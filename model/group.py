from model.person import Person


class Group:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person: Person):
        self.members.append(person)

    def remove_member(self, person: Person):
        self.members.remove(person)

    def list_members(self):
        return [member.full_name() for member in self.members]
    
    @staticmethod
    def create_group_from_input() -> 'Group':
        name = input("Enter group name: ")
        group = Group(name)
        return group