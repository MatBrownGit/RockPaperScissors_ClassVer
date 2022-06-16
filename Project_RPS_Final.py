from game_pkg import game_class_Final
from game_pkg import menu_page

menu_page.show_menupage()
game = game_class_Final.RockPaperScissors()
game.battle()


while True:
    continuePrompt = input(
        "Would you like to play again? (y/n): ").lower()
    if continuePrompt == "n":
        print("\nGoodbye.\n")
        exit()
    elif continuePrompt == "y":
        menu_page.show_menupage()
        game.battle()
    else:
        print("Invalid input")
        continue
