import datetime
from Person import*
from Student import*

list_student = []
list_student.append(Student("Roman","Bahlay", "Ihorovych",datetime.date(1997, 6, 11),"IT & Math","402","100","3" ))
list_student.append(Student("Misha","Solyan", "Volodymyrovych",datetime.date(1996, 6, 11),"IT & Math","402","200","3" ))
list_student.append(Student("Andriy","Prokopuk", "Petrovych",datetime.date(1997, 6, 11),"IT & Math","402","300","3" ))
list_student.append(Student("Uriy","Korsun", "Petrovych",datetime.date(1998, 6, 11),"IT & Math","302","100","3" ))
list_student.append(Student("Olexandr","Garbar", "Valeriyovych",datetime.date(1999, 6, 11),"IT & Math","302","2200","3" ))
list_student.append(Student("Test","Subject", "Portal",datetime.date(1997, 6, 11),"IT & Math","402","1200","3" ))
list_student.append(Student("1","2","3",datetime.date(1990,1,1),"test","1","5000","5"))


general_scholarship = 0
group_counter = 0
group = input("Група: ")
middle_age = 0
summ = 0
for obj in list_student:
    if obj.group == group:
        group_counter += 1
        summ += obj.age_general()
        general_scholarship += int(obj.scholarship)
    if summ != 0:
        middle_age = summ/group_counter
if summ != 0:
    print("=======================================")
    print("Середній вік студентів групи -->", "%.1f" % middle_age)
    print("Загальний розмір стипендії -->",general_scholarship,"грн.")
else:
    print("такої групи немає")

test = input("Вивести інфу про всіх студентів ? \n")
if test == "y":
    print("_____________________")
    for obj in list_student:
        print(obj.info())



