import datetime
class Client(object):
    def __init__(self, name, surname,address, birthdate,gender,credit,phone_numb):
        self.name = name
        self.surname = surname
        self.address = address
        self.birthdate = birthdate
        self.gender = gender
        self.credit = credit
        self.phone_numb = phone_numb


    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return print(self.name, self.surname,"is", age,"y.o.\n---------------------")

    def age_general(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


