from Person import*
import datetime

class Student(Person):
    def __init__(self, name, surname, f_name, birthdate, faculty,group,scholarship,middle_grade):
        Person.__init__(self, name, surname, f_name, birthdate)
        self.faculty = faculty
        self.scholarship = scholarship
        self.group = group
        self.middle_grade = middle_grade

    def get_details(self):
        return (self.name, self.surname, self.f_name, self.birthdate, self.faculty, self.scholarship,self.group, self.middle_grade)
       
    def info(self):
        attrs = vars(self)
        return print("\n".join("%s: %s" % item for item in attrs.items()),"\n---------------------")
        


