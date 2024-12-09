class Address:
    """
    Represents an address.
    """

    def __init__(self, street, city, state, zip_code):
        """
        Initializes a new instance of the Address class.

        Parameters
        ----------
        street : str
            The street address.
        city : str
            The city.
        state : str
            The state.
        zip_code : str
            The zip code.
        """
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def full_address(self):
        """
        Returns the full address.

        Returns
        -------
        str
            The full address.
        """
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
    

    @staticmethod
    def create_address_from_input() -> 'Address':
        """
        Creates a new Address object from user input.

        Returns
        -------
        Address
            A new Address object.
        """
        street = input("Enter street: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip code: ")
        address = Address(street, city, state, zip_code)
        
        return address