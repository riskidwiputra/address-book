from abstract.observer import Observer
from model.user import User

class ShowCurrentUserObserver(Observer):
    """
    Observer class to display the current user's information.

    Attributes:
        user (User): The user object containing user information.

    Methods:
        __call__(): Prints the current user's username in a formatted manner.
    """
    def __init__(self, user: User):
        self.user = user

    def __call__(self):
        width = 54
        title = "Address Book"
        username = f"Current User: {self.user.username}"
        print("\033[1;34m" + "=" * width + "\033[0m")
        print(f"\033[1;34m| \033[1m{title:^{width-4}}\033[0m \033[1;34m|\033[0m")
        print(f"\033[1;34m| \033[1m{username:^{width-4}}\033[0m \033[1;34m|\033[0m")
        print("\033[1;34m" + "=" * width + "\033[0m")