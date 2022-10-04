import os, sys, random, datetime

def exit_game():
    print("Thanks for playing!")
    exit()

class Duskers:
    def __init__(self):
        self.user_name, self.titanium, self.save_slots = None, 0, []
        self.encounter_scan, self.titanium_scan, self.num_robots = 0, 0, 3
        self.menu()

    def menu(self):
        print("\n║    ██████╗ ██╗   ██╗███████╗██╗  ██╗███████╗██████╗ ███████╗   ║\n"
              "║    ██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝   ║\n"
              "║    ██║  ██║██║   ██║███████╗█████╔╝ █████╗  ██████╔╝███████╗   ║\n"
              "║    ██║  ██║██║   ██║╚════██║██╔═██╗ ██╔══╝  ██╔══██╗╚════██║   ║\n"
              "║    ██████╔╝╚██████╔╝███████║██║  ██╗███████╗██║  ██║███████║   ║\n"
              "║    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ║\n")
        while True:
            print("[New] Game\n[Load] Game\n[High] Scores\n[Help]\n[Exit]")
            choice = input("\nYour command: ").lower()
            if choice == 'exit':
                return exit_game()
            elif choice == 'help':
                return self.help()
            elif choice == 'high':
                return self.scores()
            elif choice == 'new':
                self.titanium, self.num_robots, self.encounter_scan, self.titanium_scan = 0, 3, 0, 0
                return self.play_menu()
            elif choice == 'load':
                return self.load_menu()
            print("Invalid input")

    def help(self):
        print("Scan random locations for titanium. If you run out of robots, GAME OVER")
        return self.menu()

    def get_saves(self):
        for i in range(1, 4):
            if os.path.isfile(f"save_file_{i}.txt"):
                with open(f"save_file_{i}.txt", "r") as f:
                    contents = f.read()
                self.save_slots.append(contents)
            else:
                self.save_slots.append("empty")

    def load_menu(self):
        self.get_saves()
        while True:
            print("Select save slot")
            for i in range(1, 4):
                print(f"\t[{i}] {self.save_slots[i - 1]}")
            slot = int(input("\nYour command: "))
            if self.save_slots[slot - 1] != 'empty':
                break
            print("Empty slot!")
        contents = self.save_slots[slot - 1].split()
        self.user_name, self.titanium, self.num_robots, self.encounter_scan, self.titanium_scan = \
            contents[0], int(contents[2]), int(contents[4]), int(contents[10]), int(contents[12])
        print("        ║══════════════════════════════║\n"
              "        ║    GAME LOADED SUCCESSFULLY  ║\n"
              "        ║══════════════════════════════║\n")
        print(f'Welcome back, commander {self.user_name}!')
        return self.play()

    def save_menu(self, ex=False):
        self.get_saves()
        print("Select save slot")
        print(f"\t[{i}] {self.save_slots[i - 1]}" for i in range(1, 4))
        slot = int(input("Your command: "))
        with open(f"save_file_{slot}.txt", 'w') as f:
            f.write(f'{self.user_name} Titanium: {self.titanium} Robots: {self.num_robots} '
                    f'Last save: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} '
                    f'Escan: {self.encounter_scan} Tscan: {self.titanium_scan}')
        print("        ║══════════════════════════════║\n"
              "        ║    GAME SAVED SUCCESSFULLY   ║\n"
              "        ║══════════════════════════════║\n")
        return exit_game() if ex else self.play()

    def play_menu(self):
        self.user_name = input("\nEnter your name:")
        print(f"\nWelcome, commander {self.user_name}!")
        while True:
            print("Are you ready to begin?\n[Yes] [No] Return to Main[Menu]\n")
            ready = input("Your command: ").lower()
            if ready == 'menu' or ready == 'no':
                return self.menu()
            elif ready == 'yes':
                return self.play()

    def upgrade(self):
        print("║══════════════════════════════║\n"
              "║         UPGRADE STORE        ║\n"
              "║══════════════════════════════║\n"
              "║                        Price ║\n"
              "║[1] Titanium Scan         250 ║\n"
              "║[2] Enemy Encounter Scan  500 ║\n"
              "║[3] New Robot            1000 ║\n"
              "║            [Back]            ║\n"
              "║══════════════════════════════║\n")
        choice = int(input("Your command: "))
        if choice == 1 and self.titanium >= 250:
            print("Purchase successful. You can now see how much titanium you can get from each found location.")
            self.titanium -= 250; self.titanium_scan = 1
        elif choice == 2 and self.titanium >= 500:
            print("Purchase successful. You will now see how likely you will encounter an enemy at each found location.")
            self.titanium -= 500; self.encounter_scan = 1
        elif choice == 3 and self.titanium >= 1000:
            print("Purchase successful. You now have an additional robot")
            self.titanium -= 1000; self.num_robots += 1
        elif choice == 1 or choice == 2 or choice == 3:
            print("Not enough titanium")
        return self.play()

    def play(self):
        print(f"""║════════════════════════════════════════════════════════════════════════════════║

{'  ╬   ╬╬╬╬╬╬╬   ╬   ' * self.num_robots}
{'  ╬╬╬╬╬     ╬╬╬╬╬   ' * self.num_robots}
{'      ╬╬╬╬╬╬╬       ' * self.num_robots}
{'     ╬╬╬   ╬╬╬      ' * self.num_robots}
{'     ╬       ╬      ' * self.num_robots}

  Titanium: {self.titanium}
║════════════════════════════════════════════════════════════════════════════════║
║                  [Ex]plore                          [Up]grade                  ║
║                  [Save]                             [M]enu                     ║
║════════════════════════════════════════════════════════════════════════════════║""")
        while True:
            choice = input("Your command:").lower()
            if choice == 'save':
                return self.save_menu()
            elif choice == 'up':
                return self.upgrade()
            elif choice == 'm':
                return self.pause()
            elif choice == 'ex':
                return self.explore()

    def explore(self):
        max_locations, found_locations, count, choice = random.randint(1, 9), {}, 1, 's'
        while True:
            if choice == 's':
                if count <= max_locations:
                    print("Searching")
                    found_locations[str(count)] = (random.choice(locations), random.randint(10, 100), random.random())
                    for key, val in found_locations.items():
                        found = f"[{key}] {val[0]}"
                        if self.titanium_scan:
                            found += f" Titanium: {val[1]}"
                        if self.encounter_scan:
                            found += f" Encounter rate: {round(val[2] * 100)}%"
                        print(found)
                    count += 1
                    print("\n[S] to continue searching")
                else:
                    print("Nothing more in sight.\n\t[Back]")
            elif choice in found_locations:
                loc, tit, chance = found_locations[choice]
                print("Deploying robots")
                if random.random() < chance:
                    print("Enemy encounter!")
                    self.num_robots -= 1
                    if self.num_robots == 0:
                        print("Mission aborted, the last robot lost...")
                        print("        ║══════════════════════════════║\n"
                              "        ║          GAME OVER!          ║\n"
                              "        ║══════════════════════════════║\n")
                        self.save_scores()
                        return self.menu()
                    print(f"{loc} explored successfully, 1 robot lost..")
                else:
                    print(f"{loc} explored successfully, with no damage taken.")
                print(f"Acquired {tit} lumps of titanium")
                self.titanium += tit
            if choice == 'back' or choice in found_locations:
                return self.play()
            elif choice != 's':
                print("Invalid input")
            choice = input("Your command: ").lower()

    def pause(self):
        print("""                
                                ║════════════════════════║
                                ║          MENU          ║ 
                                ║════════════════════════║
                                ║     [Back] to game     ║
                                ║  Return to [Main] Menu ║
                                ║     [Save] and exit    ║
                                ║       [Exit] game      ║
                                ║════════════════════════║""")
        choice = input("\nYour command:").lower()
        if choice == 'exit':
            return exit_game()
        elif choice == 'save':
            return self.save_menu(ex=True)
        elif choice == 'back':
            return self.play()
        elif choice == 'main':
            return self.menu()

    def scores(self):
        print("\n\tHIGH SCORES\n")
        with open('high_scores.txt', 'r') as f:
            contents = sorted(f.read().strip().split('\n'), key=lambda x: int(x.split()[1]), reverse=True)
            n = 10 if len(contents) > 10 else len(contents)
            for i in range(n):
                print(f'({i + 1}) {contents[i]}')
        while input("\n\t[Back]").lower() != 'back':
            print("Invalid input")
        return self.menu()

    def save_scores(self):
        if os.path.isfile(f"high_scores.txt"):
            with open('high_scores.txt', 'r') as f:
                contents = f.read().strip().split('\n')
                contents.append(f'{self.user_name} {self.titanium}\n')
        else:
            contents = [f'{self.user_name} {self.titanium}', '\n']
        with open('high_scores.txt', 'w') as f:
            f.write('\n'.join(contents))


try:
    seed, min_anim_duration, max_anim_duration, locations = sys.argv[1:5]
except ValueError:
    seed, locations = 0, "Pee,street/Poo,park"
random.seed(seed)
locations = locations.replace(',', ' ').split("/")
game = Duskers()
