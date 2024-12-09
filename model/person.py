from model.address import Address
from typing import List, Optional


class Person:
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, addresses: Optional[List[Address]] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.addresses = addresses if addresses is not None else []

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def contact_info(self) -> str:
        return f"Email: {self.email}, Phone: {self.phone}"
    
    def add_address(self):
        address = Address.create_address_from_input()
        self.addresses.append(address)
    
    def list_addresses(self) -> List[str]:
        return [address.full_address() for address in self.addresses]

    @staticmethod
    def create_person_from_input() -> 'Person':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        person = Person(first_name, last_name, email, phone)
        
        address_count = 1
        while True:
            print("Address", address_count)
            person.add_address()
            choose = input("Do you want to add another address? (y/n): ")
            if choose.lower() != 'y':
                break
            address_count += 1

        return person