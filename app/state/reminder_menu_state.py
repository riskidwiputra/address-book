from .menu_state import MenuState
from model.user import User

class ReminderMenuState(MenuState):
    name = 'ReminderMenu'

    def __init__(self, user: User, callback):
        self.user = user
        self.callback = callback

    def show_menu(self):
        while True:
            try:
                self.callback()
                self.user.list_reminders()
                print("\033[94m======================================================")
                print("| [1] Add Reminder                                   |")
                print("| [2] Remove Reminder                                |")
                print("| [3] Back                                           |")
                print("======================================================\033[0m")
                choice = input("Enter choice: ")
                match choice:
                    case "1": self.user.add_reminder()
                    case "2": self.user.remove_reminder()
                    case "3": self.back_menu()
                    case _:
                        input("Invalid choice, please try again.")
                        break
            except:
                input("Invalid input. Please try again.")
                break
        self.show_menu()