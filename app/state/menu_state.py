from model.user import User


class MenuState(object):
    name = ''
    current_menu = []

    def change_menu(self, state: 'MenuState', **props):
        """
        Changes the current menu state to a new state.

        Args:
            state (MenuState): The new menu state class to transition to.
            **props: Additional properties to pass to the new state.

        Returns:
            None
        """
        self.current_menu.append(self.name)
        new_state = state(**props)
        self.__dict__.update(new_state.__dict__)
        self.__class__ = state
        self.show_menu()


    def back_menu(self):
        """
        Navigates back to the previous menu state.

        This method checks if there is a current menu state. If there is, it pops the last menu state from the 
        `current_menu` stack and iterates through all subclasses of `MenuState` to find the matching state class 
        by name. Once found, it updates the current instance's dictionary and class to match the previous state 
        and displays the menu.

        Raises:
            AttributeError: If `current_menu` is empty or if no matching state class is found.
        """
        if self.current_menu:
            previous_menu_name = self.current_menu.pop()
            for state_class in MenuState.__subclasses__():
                if state_class.name == previous_menu_name:
                    previous_state = state_class(user=self.user, callback=self.callback)
                    self.__dict__.update(previous_state.__dict__)
                    self.__class__ = state_class
                    self.show_menu()
                    break

    def clear_terminal(self):
        """
        Clears the terminal screen.

        This method is responsible for clearing the terminal screen. It is called by the `ClearTerminalObserver` 
        observer class when the `Application` class changes the menu state.

        Returns:
            None
        """
        print("\033c", end='')


    def show_menu(self):
        """
        Displays the menu to the user.

        This method is responsible for rendering and presenting the menu options
        to the user. It does not take any parameters and does not return any value.
        """
        pass