from model.person import Person
from model.group import Group
from model.reminder import Reminder
from typing import List
from tabulate import tabulate

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.contacts: List[Person] = []
        self.groups: List[Group] = []
        self.reminder: List[Reminder] = []


    def add_contact(self):
        person: Person = Person.create_person_from_input()
        self.contacts.append(person)


    def remove_contact(self):
        person = self.choose_contact()
        self.contacts.remove(person)


    def list_contacts(self):
        table = []
        for i, person in enumerate(self.contacts):
            addresses = person.list_addresses()
            first_address = addresses[0] if addresses else ""
            row = [i + 1, person.full_name(), person.email, person.phone, first_address]
            table.append(row)
            for address in addresses[1:]:
                table.append(["", "", "", "", address])
        print(tabulate(table, headers=["No", "Name", "Email", "Phone", "Address"], tablefmt="simple"))


    def choose_contact(self):
        try:
            self.list_contacts()
            choice = int(input("Enter the number of the contact you want to choose: "))
            if 1 <= choice < len(self.contacts) + 1:
                return self.contacts[choice - 1]
            else:
                print("Invalid choice. Please try again.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None


    def add_group(self):
        group = Group.create_group_from_input()
        self.groups.append(group)


    def remove_group(self):
        group = self.choose_group()
        self.groups.remove(group)


    def list_groups(self):
        table = []
        for i, person in enumerate(self.groups):
            members = [member.full_name() for member in person.members]
            first_member = members[0] if members else ""
            row = [i + 1, person.name, first_member]
            table.append(row)
            for member in members[1:]:
                table.append(["", "", member])
        print(tabulate(table, headers=["No", "Group Name", "Members"], tablefmt="simple"))


    def choose_group(self) -> Group:
        try:
            self.list_groups()
            choice = int(input("Enter the number of the group you want to choose: "))
            if 1 <= choice < len(self.groups) + 1:
                return self.groups[choice - 1]
            else:
                print("Invalid choice. Please try again.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
        
    
    def add_member_to_group(self):
        group = self.choose_group()
        if group:
            person = self.choose_contact()
            if person:
                group.add_member(person)



    def add_reminder(self):
        reminder = Reminder.create_reminder_from_input()
        self.reminder.append(reminder)


    def list_reminders(self):
        table = []
        for i, reminder in enumerate(self.reminder):
            row = [i + 1, reminder.title, reminder.date, reminder.time, reminder.description]
            table.append(row)
        print(tabulate(table, headers=["No", "Title", "Date", "Time", "Description"], tablefmt="simple"))


    def remove_reminder(self):
        reminder = self.choose_reminder()
        self.reminder.remove(reminder)


    def choose_reminder(self) -> Reminder:
        try:
            self.list_reminders()
            choice = int(input("Enter the number of the reminder you want to choose: "))
            if 1 <= choice < len(self.reminder) + 1:
                return self.reminder[choice - 1]
            else:
                print("Invalid choice. Please try again.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
    

    @staticmethod
    def create_user_from_input() -> 'User':
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = User(username, password)
        
        return user