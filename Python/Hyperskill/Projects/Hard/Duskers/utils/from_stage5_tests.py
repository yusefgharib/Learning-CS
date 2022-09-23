import glob
from utils.global_tests import SharedTest, DEFAULT_CLI_ARGS, run_for_stages, get_hub_lines, check_graphical_robots, \
    GlobalDuskersTest
from utils.from_stage4_tests import (SAVE_FILE_NAME, FromStage4DuskersTest,
                                     file_cleanup, tests, TestAlg, restart)
from hstest import CheckResult, TestedProgram, dynamic_test
from datetime import datetime, timedelta

MODULE_NAME = 'duskers.duskers'
STAGE_NO = 5

NOT_FOUND_MSG = "{} not found in save slot.\n" \
                "Please check your game saving logic and display the " \
                "specified data in the right format in the load menu."


def timestamp_with_seconds(time: datetime = datetime.today()):
    return str(time)[:16]


class DuskersTest(SharedTest):
    @staticmethod
    def test_save(pr: TestedProgram, username: str) -> CheckResult:
        save_time = datetime.today()
        pr = restart(pr, DEFAULT_CLI_ARGS)

        load_menu = pr.execute("load")

        expected_data_in_load_menu = {
            "player name": username,
            "titanium balance": 0,
            "robot count": 3,
        }

        for element, value in expected_data_in_load_menu.items():
            if str(value) not in load_menu:
                return CheckResult.wrong(
                    NOT_FOUND_MSG.format(element.capitalize())
                )

        # tolerate 1 sec difference in recorded save time
        valid_save_timestamps = [timestamp_with_seconds(date) for date in
                                 [save_time, save_time - timedelta(seconds=1)]
                                 ]

        if not any(timestamp in load_menu for timestamp in valid_save_timestamps):
            return CheckResult.wrong(
                NOT_FOUND_MSG.format("Last saved time")
            )

        if len([line for line in load_menu.lower().splitlines()
                if "empty" in line]) != 2:
            return CheckResult.wrong(
                "There should be exactly two slots displaying 'empty' "
                "when 1 slot is occupied by save data."
            )

        if len(glob.glob(SAVE_FILE_NAME)) < 1:
            return CheckResult.wrong(
                f"No file with '{SAVE_FILE_NAME}' within the filename found.\n"
                "Please make sure all save files have this '{SAVE_FILE_NAME}' "
                "in their name and are created in the directory of program "
                "execution."
            )

        return CheckResult.correct()

    @dynamic_test
    def test_updated_menu(self):
        pr = TestedProgram()
        main_menu = pr.start(*DEFAULT_CLI_ARGS).lower()

        if "load" not in main_menu or "new" not in main_menu:
            return CheckResult.wrong("The player should now have the option"
                                     "of choosing to start a [New] game or to [Load] a game.")

        return CheckResult.correct()

    @dynamic_test
    @file_cleanup
    def test_load_with_no_saves(self):
        pr = TestedProgram()
        pr.start(*DEFAULT_CLI_ARGS)
        load_menu = pr.execute("load").lower()

        if len([line for line in load_menu.splitlines() if "empty" in line]) != 3:
            return CheckResult.wrong(
                "There should be exactly three slots displaying 'empty' upon "
                "initially starting the game and choosing the 'load' option."
            )

        return CheckResult.correct()

    @dynamic_test(data=["Hyperskill", "explorer", "random"])
    @file_cleanup
    def test_save_file_created_after_saving_new_game(self, username):
        pr = TestedProgram()
        pr.start(*DEFAULT_CLI_ARGS)
        for command in ["new", username, "yes", "save", "1"]:
            pr.execute(command)

        return self.test_save(pr, username)

    @dynamic_test(data=tests)
    @run_for_stages(5)
    @file_cleanup
    def save_file_created_after_saving_game(self, test: TestAlg):
        username = "hyperskill"
        cli_args = (test.seed, "0", "0", test.places)

        pr = TestedProgram()
        pr.start(*cli_args)
        for command in ["new", username, "yes", *test.input, "save", "1"]:
            pr.execute(command)

        return self.test_save(pr, username)

    @dynamic_test(data=tests)
    @run_for_stages(5)
    @file_cleanup
    def test_data_loaded_into_game(self, test: TestAlg):
        username = "hyperskill"
        cli_args = (test.seed, "0", "0", test.places)

        pr = TestedProgram()
        pr.start(*cli_args)
        for command in ["new", username, "yes", *test.input, "save", "1"]:
            pr.execute(command)

        # regeneration of test data runs before starting new program instance to
        # not mess with the seed
        starting_titanium = test.expected
        test.regenerate(1)
        new_titanium = str(int(test.expected) + int(starting_titanium))

        pr = restart(pr, cli_args, ["load"])
        loaded_game = pr.execute("1")

        if username not in loaded_game:
            return CheckResult.wrong("Player not greeted after loading the game")

        if starting_titanium not in loaded_game:
            return CheckResult.wrong(
                "Wrong titanium balance displayed after loading game."
            )

        if "║" not in loaded_game:
            return CheckResult.wrong(
                "Please make sure your HUB begins with a '║' character for "
                "testing.\n"
                "Make sure the HUB is displayed after loading the game."
            )

        hub_lines = get_hub_lines(loaded_game)

        if len(hub_lines) < 7:
            return CheckResult.wrong(
                "Hub not displayed properly, look at the examples for help.\n"
                "Make sure the first line of the hub begins with a '║' character"
            )

        if not check_graphical_robots(hub_lines, 3):
            return CheckResult.wrong(
                "Robots loaded into the game hub incorrectly."
            )

        for command in test.input:
            game_output = pr.execute(command)

        if new_titanium not in game_output:
            return CheckResult.wrong(
                "Titanium balance not updated correctly after loading game "
                "and exploring."
            )

        return CheckResult.correct()

    @dynamic_test(data=tests[0:2])
    @run_for_stages(5)
    @file_cleanup
    def test_multiple_save_slots(self, test: TestAlg):
        titanium_balances = []

        for slot in range(1, 4):
            username = "hyperskill"
            cli_args = (test.seed, "0", "0", test.places)

            pr = TestedProgram()
            pr.start(*cli_args)
            for command in ["new", username, "yes", *test.input, "save", str(slot)]:
                pr.execute(command)

            titanium_balances.append(test.expected)
            pr.stop()
            test.regenerate(test.data.explorations + 1)

        pr = TestedProgram()
        pr.start(*cli_args)
        load_menu = pr.execute("load")

        if len([line for line in load_menu.splitlines() if "empty" in line]) > 0:
            return CheckResult.wrong(
                "After to 3 different slots, there should not be any save "
                "slots that read 'empty' in the load menu."
            )

        for slot in range(1, 4):
            loaded_game = pr.execute(str(slot))
            if titanium_balances[slot - 1] not in loaded_game:
                return CheckResult.wrong(
                    "Wrong titanium balance displayed after loading game "
                    "where multiple save slots are occupied."
                )

            pr = restart(pr, cli_args)
            load_menu = pr.execute("load")

        return CheckResult.correct()


if __name__ == '__main__':
    # run tests that are shared among more than 1 stage
    return_code = GlobalDuskersTest(STAGE_NO, MODULE_NAME).run_tests()[0]
    # run tests specific to this stage if global tests pass

    suites = [
        FromStage4DuskersTest(STAGE_NO, MODULE_NAME),
        DuskersTest(STAGE_NO, MODULE_NAME)]
    current_suite = 0

    while return_code == 0 and current_suite < len(suites):
        return_code = suites[current_suite].run_tests()[0]
        current_suite += 1
