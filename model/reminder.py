class Reminder:
    """
    Represents a reminder.
    """

    def __init__(self, title, date, time, description):
        """
        Initializes a new instance of the Reminder class.

        Parameters
        ----------
        title : str
            The title of the reminder.
        date : str
            The date of the reminder.
        time : str
            The time of the reminder.
        description : str
            The description of the reminder.
        """
        self.title = title
        self.date = date
        self.time = time
        self.description = description

    def reminder_info(self):
        """
        Returns the reminder information.

        Returns
        -------
        str
            The reminder information.
        """
        return f"Reminder: {self.title} on {self.date} at {self.time}. Description: {self.description}"
    

    @staticmethod
    def create_reminder_from_input():
        """
        Creates a new reminder from user input.

        Returns
        -------
        Reminder
            The new reminder object.
        """
        title = input("Enter reminder title: ")
        date = input("Enter reminder date: ")
        time = input("Enter reminder time: ")
        description = input("Enter reminder description: ")
        return Reminder(title, date, time, description)