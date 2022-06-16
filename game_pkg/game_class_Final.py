import random
import time


class RockPaperScissors:
    weaponsString = ["Rock", "Paper", "Scissors"]

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.player = ""
        self.computer = ""

    def getValueForWeapon(self, weaponsString):
        if weaponsString == "Rock":
            return 0
        elif weaponsString == "Paper":
            return 1
        elif weaponsString == "Scissors":
            return 2

    def getUserInput(self):
        while True:
            playerInput = input("Choose your weapon: ")
            if playerInput == "1" or playerInput.lower() == "rock":
                print("You have chosen: Rock!")
                self.player = self.weaponsString[0]
                return
            elif playerInput == "2" or playerInput.lower() == "paper":
                print("You have chosen: Paper!")
                self.player = self.weaponsString[1]
                return
            elif playerInput == "3" or playerInput.lower() == "scissors":
                print("You have chosen: Scissors!")
                self.player = self.weaponsString[2]
                return
            else:
                print("Unknown Weapon")
                continue

    def getComputerChoice(self):
        self.computer = random.choice(self.weaponsString)
        print("Computer has chosen...", self.computer + "!")

    def battle(self):
        self.getUserInput()
        print("Computer thinking...")
        time.sleep(1)
        self.getComputerChoice()
        result = (self.getValueForWeapon(self.player) -
                  self.getValueForWeapon(self.computer)) % 3
        if result == 0:
            self.ties += 1
            print("\nDouble knockout! Tied battle!")
        elif result == 1:
            self.wins += 1
            self.getWinMessageForWeapon(self.player)
            print("\nYOU ARE VICTORIOUS!!!")
        elif result == 2:
            self.losses += 1
            self.getWinMessageForWeapon(self.computer)
            print("\nYou are beaten!")

        print("\nWins: ", self.wins)
        print("Losses: ", self.losses)
        print("Ties: ", self.ties, "\n")

    def getWinMessageForWeapon(self, weapon):
        if weapon == "Rock":
            print("\nRock crushes scissors!")
        elif weapon == "Paper":
            print("\nPaper covers rock!")
        elif weapon == "Scissors":
            print("\nScissors cuts paper!")
