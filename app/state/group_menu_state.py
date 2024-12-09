from .menu_state import MenuState
from model.user import User

class GroupMenuState(MenuState):
    name = 'GroupMenu'

    def __init__(self, user: User, callback):
        self.user = user
        self.callback = callback


    def show_menu(self):
        while True:
            self.callback()
            self.user.list_groups()
            print("\033[94m======================================================")
            print("| [1] Add Group                                       |")
            print("| [2] Add Member                                      |")
            print("| [3] Remove Group                                    |")
            print("| [4] Back                                            |")
            print("======================================================\033[0m")
            choice = input("Enter choice: ")
            match choice:
                case "1": self.user.add_group()
                case "2": self.user.add_member_to_group()
                case "3": self.user.remove_group()
                case "4": self.back_menu()
                case _:
                    print("Invalid choice, please try again.")
                    break
        self.show_menu()