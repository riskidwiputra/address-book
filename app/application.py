from model.user import User
from app.state import MenuState, MainMenuState
from observer.show_current_user_observer import ShowCurrentUserObserver
from observer.clear_terminal_observer import ClearTerminalObserver
from observer.loading_observer import LoadingObserver

class Application:
    _instance = None
    _main_menu = 'main menu'
    _contact_menu = 'contact menu'
    _group_menu = 'group menu'
    _reminder_menu = 'reminder menu'


    def __init__(self):
        self.user = None
        self.observers = []
        self.current_menu = []
        self.state: MenuState = MenuState()


    def run(self):
        self.user = User.create_user_from_input()
        self.register_observers()
        self.change_menu(MainMenuState)

    
    def __new__(cls):
        """
        Create a new instance of the class if one does not already exist.

        This method ensures that only one instance of the class is created (Singleton pattern).
        If an instance already exists, it returns the existing instance.

        Returns:
            Main: The single instance of the class.
        """
        if not cls._instance:
            cls._instance = super(Application, cls).__new__(cls)
        return cls._instance
    

    def register_observers(self):
        self.observers.append(ClearTerminalObserver())
        self.observers.append(ShowCurrentUserObserver(self.user))
        self.observers.append(LoadingObserver())


    def change_menu(self, state: MenuState):
        """
        Changes the current menu state and notifies observers of the change.

        Args:
            state (MenuState): The new state to change the menu to.
        """
        self.notify_observers()
        self.state.change_menu(state, user=self.user, callback=self.notify_observers)


    def notify_observers(self):
        for observer in self.observers:
            observer()