import os
from abstract.observer import Observer

class ClearTerminalObserver(Observer):
    """
    ClearTerminalObserver is an observer class that clears the terminal screen
    when called. It inherits from the Observer base class.

    Methods:
        __call__(): Clears the terminal screen. Uses 'cls' command for Windows
                    and 'clear' command for Unix-based systems.
    """
    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')