class user:
    def __init__(self,username, password):
        self.username = username
        self.password = password

class person:
    def __init__(self, name, email,phoneNum):
        self.nama = name
        self.email = email
        self.phoneNum = phoneNum

class city(person):
    def __init__(self, nama, email, phoneNum, street, district, city, province):
        super().__init__(nama, email, phoneNum)
        self.street = street
        self.district = district
        self.city = city
        self.street = street
        self.province = province

class village(person):
    def __init__(self, nama, email, phoneNum, street, village, province):
        super().__init__(nama, email, phoneNum)
        self.street = street
        self.village = village
        self.street = street
        self.province = province

class adddress:
    def __init__(self):
        self.list = []

class group:
    def __init__(self, groupName):
        self.groupName = groupName
        self.list = []
    def add(self, person):
        self.list.append(person)

class reminder:
    def __init__(self, person, message):
        self.person = person
        self.message = message