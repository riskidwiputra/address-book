import sys
from app.state import MenuState, ContactMenuState, GroupMenuState, ReminderMenuState
from model.user import User

class MainMenuState(MenuState):
    name = 'main menu'

    def __init__(self, user: User, callback):
        self.user = user
        self.callback = callback

    def show_menu(self):
        while True:    
            self.callback()
            print("\033[94m======================================================")
            print("| [1] Contact                                        |")
            print("| [2] Group                                          |")
            print("| [3] Reminder                                       |")
            print("| [4] Logout                                         |")
            print("======================================================\033[0m")
            choice = input("Enter choice: ")
            match choice:
                case "1": self.change_menu(ContactMenuState, user=self.user, callback=self.callback)
                case "2": self.change_menu(GroupMenuState, user=self.user, callback=self.callback)
                case "3": self.change_menu(ReminderMenuState, user=self.user, callback=self.callback)
                case "4": sys.exit()
                case _:
                    print("Invalid choice, please try again.")
