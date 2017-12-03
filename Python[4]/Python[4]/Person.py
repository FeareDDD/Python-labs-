import datetime
class Person(object):
   def __init__(self, name, surname, f_name, birthdate):
        self.name = name
        self.surname = surname
        self.f_name = f_name
        self.birthdate = birthdate


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

   def info(self):
        attrs = vars(self)
        return print( '\n'.join("%s: %s" % item for item in attrs.items()),"\n---------------------")
        




