from typing import List, Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from hstest.exceptions import WrongAnswerException


class RobogotchiTestParent(StageTest):

    def prs_print_check(self, output, answer):
        parsed_output = output.split()[:-4]
        try:
            robot_answer = parsed_output[2] if parsed_output[1] == 'chose' else parsed_output[3]
            ideal = self.check_who_won_ro(robot_answer=robot_answer,
                                          human_answer=answer).split('\n')
            ideal = [line for line in ideal if line]
            for i in ideal:
                if i.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                               f"{i}")
            return True
        except IndexError:
            pass

    def check_who_won_num(self, human_answer, robot_answer, goal):
        if abs(goal - human_answer) < abs(goal - robot_answer):
            self.won_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nYou won!")
        elif abs(goal - human_answer) > abs(goal - robot_answer):
            self.lost_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nRobot won!")
        else:
            self.draw_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nIt's a draw!")

    def check_who_won_ro(self, human_answer, robot_answer):
        if human_answer == 'paper':
            if robot_answer == 'scissors':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'rock':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        elif human_answer == 'rock':
            if robot_answer == 'paper':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'scissors':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        elif human_answer == 'scissors':
            if robot_answer == 'rock':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'paper':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        else:
            return 'No such option! Try again!\n'

    def interface_prints_check(self, output):
        interface_parsed = self.ideal_interface.split('\n')
        output = output.lower()
        for inter in interface_parsed:
            if inter.lower().strip() not in output:
                raise WrongAnswerException(f"The following string is not found in your menu output:\n"
                                           f"{inter}")
        return True

    def oil_what_prints(self, output):
        if (self.rust == 0) and ('fine' in output):
            if "Daneel is fine, no need to oil" not in output:
                return False
        elif self.boredom == 100:
            if "Daneel is too bored" not in output:
                return False
        else:
            i = 10 if 'was 10' in output else 20
            text = f"Daneel's level of rust was {self.rust + i}. Now it is {self.rust}." \
                   f"\nDaneel is less rusty"
            text = text.split('\n')
            for tex in text:
                if tex.lower().strip() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def recharge_what_prints(self, output):
        if self.battery == 100 and 'level' not in output:
            if "Daneel is charged" not in output:
                return False
        else:
            if self.battery != 100:
                message = '\nDaneel is recharged'
                text = f"Daneel's level of overheat was {self.overheat + 5}. Now it is {self.overheat}." \
                       f"\nDaneel's level of the battery was {self.battery - 10}. Now it is {self.battery}." \
                       f"\nDaneel's level of boredom was {self.boredom - 5}. Now it is {self.boredom}.\n" \
                       f"{message}"
                text = text.split('\n')
                for tex in text:
                    if tex.lower() not in output.lower():
                        raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                                   f"{tex}")
        return True

    def sleep_what_prints(self, output):
        if self.overheat == 0:
            if "Daneel is cool" not in output:
                return False
        else:
            if self.overheat != 0:
                insertion = '\nDaneel cooled off'
            else:
                insertion = '\nDaneel is cool'
            text = f"Daneel's level of overheat was {self.overheat + 20}. Now it is {self.overheat}.\n" \
                   f"{insertion}"
            text = text.split('\n')
            for tex in text:
                if tex.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def learn_changes(self, output):
        if self.skills != 100:
            text = f"Daneel's level of skill was {self.skills - 10}. Now it is {self.skills}." \
                   f"\nDaneel's level of overheat was {self.overheat - 10}. Now it is {self.overheat}." \
                   f"\nDaneel's level of the battery was {self.battery + 10}. Now it is {self.battery}." \
                   f"\nDaneel's level of boredom was {self.boredom - 5}. Now it is {self.boredom}." \
                   f"\n\nDaneel has become smarter!"
            if self.battery < 10:
                text += f"\nDaneel's level of rust was {self.rust - 50}. Now it is {self.rust}."
                text += '\nGuess what! Daneel fell into the pool!'
            if 10 <= self.battery < 30:
                text += f"\nDaneel's level of rust was {self.rust - 10}. Now it is {self.rust}."
                text += "\nOh no, Daneel stepped into a puddle!"
            text = text.split('\n')
            for tex in text:
                if tex.lower().strip() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                               f"{tex}")
        return True

    def game_statistics_prints_check(self, output, game):
        if game == 'numbers':
            ideal = f"You won: {self.won_numbers}," \
                    f"\nRobot won: {self.lost_numbers}," \
                    f"\nDraws: {self.draw_numbers}."
            ideal = ideal.split('\n')
            for i in ideal:
                if i.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                               f"{i}")
        else:
            ideal = f"You won: {self.won_roshambo}," \
                    f"\nRobot won: {self.lost_roshambo}," \
                    f"\nDraws: {self.draw_roshambo}."
            ideal = ideal.split('\n')
            for i in ideal:
                if i.lower() not in output.lower():
                    raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                               f"{i}")
        return True

    def increase_the_params(self, command):
        if command == 'learn':
            self.skills += 10
            self.overheat = self.overheat + 10 if self.overheat + 10 <= 100 else 100
            self.battery = self.battery - 10 if self.battery - 10 > 0 else 0
            self.boredom = self.boredom + 5 if self.boredom + 5 < 100 else 100
            if self.battery < 10:
                self.rust += 50
            if 30 > self.battery >= 10:
                self.rust += 10
        elif command == 'play':
            self.boredom = self.boredom - 20 if self.boredom - 20 >= 0 else self.boredom - self.boredom
            self.overheat = self.overheat + 10 if self.overheat + 10 < 100 else 100
        elif command == 'work':
            self.boredom = self.boredom + 10 if self.boredom + 10 < 100 else 100
            self.overheat = self.overheat + 10 if self.overheat + 10 < 100 else 100
            self.battery = self.battery - 10 if self.battery - 10 > 0 else 0
            if self.battery < 10:
                self.rust += 50
            if 30 > self.battery >= 10:
                self.rust += 10
        elif command == 'oil':
            self.rust = self.rust - 20 if self.rust - 20 > 0 else self.rust - self.rust
        elif command == 'sleep':
            self.overheat = self.overheat - 20 if self.overheat - 20 > 0 else self.overheat - self.overheat
        elif command == 'recharge':
            self.overheat = self.overheat - 5 if self.overheat - 5 > 0 else 0
            self.battery = self.battery + 10 if self.battery + 10 < 100 else 100
            self.boredom = self.boredom + 5 if self.boredom + 5 < 100 else 100

    def play_what_prints_check(self, output):
        if "which game would you like to play?" not in output.lower():
            return False
        return True

    def roshambo_what_prints_check(self, output):
        if "what is your move?" not in output.lower():
            return False
        return True

    def work_what_prints(self, output):
        if self.skills < 50:
            if 'Daneel has got to learn before working' not in output:
                return False
        text = f"\nDaneel's level of overheat was {self.overheat - 10}. Now it is {self.overheat}." \
               f"\nDaneel's level of the battery was {self.battery + 10}. Now it is {self.battery}." \
               f"\nDaneel's level of boredom was {self.boredom - 10}. Now it is {self.boredom}." \
               f"\n\nDaneel did well!"
        if self.battery < 10:
            text += f"\nDaneel's level of rust was {self.rust - 50}. Now it is {self.rust}."
            text += '\nGuess what! Daneel fell into the pool!'
        if 10 <= self.battery < 30:
            text += f"\nDaneel's level of rust was {self.rust - 10}. Now it is {self.rust}."
            text += "\nOh no, Daneel stepped into a puddle!"
        text = text.split('\n')
        for tex in text:
            if tex.lower().strip() not in output.lower():
                raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                           f"{tex}")
        return True

    def wrong_option_what_prints(self, output):
        check = "invalid input" in output.lower() and 'try again' in output.lower()
        if not check:
            return False
        return True

    def info_what_prints(self, output):
        text = f"Daneel's stats are:" \
               f"\nbattery is {self.battery}," \
               f"\noverheat is {self.overheat}," \
               f"\nskill level is {self.skills}," \
               f"\nboredom is {self.boredom}," \
               f"\nrust is {self.rust}."
        text = text.split('\n')
        for tex in text:
            if tex.strip().lower() not in output.lower():
                raise WrongAnswerException(f"The following line is not found in your info output:\n"
                                           f"{tex}")
        return True

    def parse_the_output(self, output):
        parsed_output = output.split()
        check = len(parsed_output) >= 11 and isinstance(int(parsed_output[5].strip('.')), int) \
                and isinstance(int(parsed_output[10].strip('.')), int)
        if not check:
            raise WrongAnswerException("The result of the game is formatted incorrectly")
        else:
            robot_answer = int(parsed_output[5].strip('.'))
            goal_number = int(parsed_output[10].strip('.'))
        return robot_answer, goal_number

    def normal_number_prints_check(self, output, number):
        try:
            parsed_output = output.split()
            try:
                robot_answer = int(parsed_output[5].strip('.'))
                goal_number = int(parsed_output[10].strip('.'))
            except IndexError:
                raise WrongAnswerException("Make sure your output is shaped after the examples")
            ideal = self.check_who_won_num(number, robot_answer, goal_number).split('\n')
            ideal = [line for line in ideal if line][-1]
            if ideal.lower() not in output.lower():
                raise WrongAnswerException(f"The following line is not found in your game output:\n"
                                           f"{ideal}")
            return True
        except ValueError:
            return False

    def numbers_what_prints_check(self, output):
        if 'what is your number?' not in output.lower():
            return False
        return True

    def numbers_exceptions(self, output, kind):
        output = [line for line in output.lower().split('\n') if line][0]
        if isinstance(kind, str):
            if "a string is not a valid input" not in output:
                return False
        elif kind > 1000000:
            if "the number can't be bigger than 1000000" not in output:
                return False
        elif kind < 0:
            if "number can't be negative" not in output:
                return False
        return True

    def knife_exception(self, output):
        check = 'no such option' in output.lower() and 'try again' in output.lower()
        if not check:
            return False
        return True

    def zerify_numbers_count(self, game):
        if game == 'numbers':
            self.won_numbers = 0
            self.lost_numbers = 0
            self.draw_numbers = 0
        else:
            self.won_roshambo = 0
            self.lost_roshambo = 0
            self.draw_roshambo = 0

    def fresh_start(self):
        self.skills = 0
        self.overheat = 0
        self.boredom = 0
        self.battery = 100
        self.rust = 0

        self.boredom_previous = 0
        self.rust_previous = 0


class RobogotchiTest1(RobogotchiTestParent):
    ideal_interface = "\nAvailable interactions with Daneel:" \
                      "\nexit\ninfo" \
                      "\nwork" \
                      "\nplay" \
                      "\noil" \
                      "\nrecharge" \
                      "\nsleep" \
                      "\nlearn\n" \
                      "\nChoose:"

    won_roshambo = 0
    lost_roshambo = 0
    draw_roshambo = 0

    won_numbers = 0
    lost_numbers = 0
    draw_numbers = 0

    skills = 0
    overheat = 0
    boredom = 0
    battery = 100
    rust = 0

    boredom_previous = 0
    rust_previous = 0

    def generate(self) -> List[TestCase]:

        return [
            # TestCase(stdin=[self.func1, self.func2, self.func3, self.func4, self.func5, self.func6, self.func7]),
            # TestCase(stdin=[self.func8, self.func9, self.func10, self.func11, self.func12, self.func13, self.func14,
            #                self.func15, self.func16, self.func17]),
            # TestCase(stdin=[self.func18, self.func19, self.func20, self.func21, self.func22, self.func23, self.func24,
            #                self.func25, self.func26, self.func27, self.func28, self.func29, self.func30, self.func31,
            #                self.func32, self.func33, self.func34]),
            TestCase(stdin=[self.func35, self.func36, self.func37, self.func38, self.func39, self.func40,
                            self.func41, self.func42, self.func43, self.func44, self.func45,
                            self.func46, self.func47, self.func48, self.func49], check_function=self.check_rust),
            TestCase(stdin=[self.func35, self.func36, self.func37, self.func38, self.func39, self.func40,
                            self.func41, self.func42, self.func43, self.func44, self.func45,
                            self.func46, self.func47, self.func48, self.func50], check_function=self.check_rust),
            TestCase(stdin=[self.func35, self.func36, self.func37, self.func38, self.func39, self.func40,
                            self.func41, self.func42, self.func43, self.func44,
                            self.func51], check_function=self.check_boom)
        ]

    """Test 1"""

    def func1(self, output):
        if output.strip() != 'How will you call your robot?':
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func2(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'info'

    def func3(self, output):
        if not self.info_what_prints(output):
            return CheckResult.wrong("The information provided is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'oil'

    def func4(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The program should print that the robot doesn't need oiling")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'recharge'

    def func5(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The program should print that the robot is charged")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'sleep'

    def func6(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The program should print that the robot is cool")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func7(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'exit'

    """Test 2"""

    def func8(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func9(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func10(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The stats message is incorrect")
        self.boredom_previous = self.boredom
        self.rust_previous = self.rust
        self.increase_the_params('play')
        return 'play'

    def func11(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should ask the user which game to play")
        return 'roshambo'

    def func12(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'paper'

    def func13(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func14(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        self.zerify_numbers_count('roshambo')
        self.rust_previous = self.rust
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'work'

    def func15(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong("The user should be informed that the robot needs to learn")
        return 'fly to the moon'

    def func16(self, output):
        if not self.wrong_option_what_prints(output):
            return CheckResult.wrong("The user should be informed about incorrect input")
        self.increase_the_params('learn')
        return 'learn'

    def func17(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The stats message is incorrect")
        return 'exit'

    """Test 3"""

    def func18(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func19(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func20(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func21(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func22(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func23(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func24(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func25(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong('The parameters were not changed correctly after working')
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one.")
        self.increase_the_params('oil')
        return 'oil'

    def func26(self, output):
        if not self.oil_what_prints(output):
            return CheckResult.wrong("The robot should be oiled properly.")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one.")
        self.rust_previous = self.rust
        self.increase_the_params('work')
        return 'work'

    def func27(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong('The parameters were not changed correctly after working')
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one.")
        self.increase_the_params('learn')
        return 'learn'

    def func28(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('sleep')
        return 'sleep'

    def func29(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func30(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func31(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'learn'

    def func32(self, output):
        if 'the level of the battery is 0, daneel needs recharging' not in output.lower():
            return CheckResult.wrong("The robot must have run out of the battery by now")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'sleep'

    def func33(self, output):
        if 'the level of the battery is 0, daneel needs recharging' not in output.lower():
            return CheckResult.wrong("The robot must have run out of the battery by now")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func34(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'exit'

    "Test 4"

    def func35(self, output):
        self.fresh_start()
        if 'how will you call your robot?' not in output.lower():
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func36(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func37(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func38(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func39(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func40(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func41(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('work')
        return 'work'

    def func42(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong('The parameters were not changed correctly after working')
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('work')
        return 'work'

    def func43(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong('The parameters were not changed correctly after working')
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func44(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('learn')
        return 'learn'

    def func45(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('sleep')
        return 'sleep'

    def func46(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The program should print that the robot is cool")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('work')
        return 'work'

    def func47(self, output):
        if not self.work_what_prints(output):
            return CheckResult.wrong('The parameters were not changed correctly after working')
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'work'

    def func48(self, output):
        if 'the level of the battery is 0, daneel needs recharging' not in output.lower():
            return CheckResult.wrong("The robot must have run out of the battery by now")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('recharge')
        return 'recharge'

    def func49(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'work'

    "Test 5"

    def func50(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'learn'

    "Test 6"

    def func51(self, output):
        if not self.learn_changes(output):
            return CheckResult.wrong("The robot learnt something wrong")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'work'

    def check(self, reply: str, attach: Any) -> CheckResult:
        if 'game over' not in reply.lower():
            return CheckResult.wrong("The program should print that the game is over")
        return CheckResult.correct()

    def check_boom(self, reply: str, attach: Any) -> CheckResult:
        check = 'the level of overheat reached 100, daneel has blown up' in reply.lower()
        check2 = 'game over' in reply.lower() and 'try again?' in reply.lower()
        if not (check and check2):
            return CheckResult.wrong("The program should print that the game is over")
        return CheckResult.correct()

    def check_rust(self, reply: str, attach: Any) -> CheckResult:
        check = 'daneel is too rusty' in reply.lower() and 'game over' in reply.lower() and 'try again?' in reply.lower()
        if not check:
            return CheckResult.wrong("The robot should be too rusty by now")
        return CheckResult.correct()


if __name__ == '__main__':
    RobogotchiTest1().run_tests()
