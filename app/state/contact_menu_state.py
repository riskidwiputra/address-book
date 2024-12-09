from .menu_state import MenuState
from model.user import User

class ContactMenuState(MenuState):
    name = 'ContactMenu'

    def __init__(self, user: User, callback):
        """
        Initializes the ContactMenuState with a user and a callback function.

        Args:
            user (User): The user object associated with this state.
            callback (Callable): A callback function to be executed.
        """
        self.user: User = user
        self.callback = callback

    def show_menu(self):
        while True:
            self.callback()
            self.user.list_contacts()
            print("\033[94m======================================================")
            print("| 1. Add Contact                                     |")
            print("| 2. Remove Contact                                  |")
            print("| 3. Back                                            |")
            print("======================================================\033[0m")
            choice = input("Enter choice: ")
            match choice:
                case "1": self.user.add_contact()
                case "2": self.user.remove_contact()
                case "3": self.back_menu()
                case _:
                    print("Invalid choice, please try again.")
                    break
            self.show_menu()