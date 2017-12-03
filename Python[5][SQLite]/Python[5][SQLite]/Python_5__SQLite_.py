import sqlite3 as db
c = db.connect(database="bank")
cu = c.cursor()
flag = False
def deleteTable():
    try:
        cu.execute("""DROP TABLE user;""")
    except db.DatabaseError as x:
        print("Hi: ", x)
        c.commit()
        c.close()

def createTable():
    try:
        cu.execute("""
            CREATE TABLE user (
                id INTEGER PRIMARY KEY,
                name VARCHAR(30),
                surname VARCHAR(30),
                address VARCHAR(50),
                birth_date DATE,
                gender VARCHAR(6),
                credit INTEGER,
                phone_numb VARCHAR(13)
                );
            """)
    except db.DatabaseError as x:
        print("Hi: ", x)
        c.commit()
#deleteTable()
#createTable()
if flag:
    cu.execute("""
            INSERT INTO user (
                id,name,surname,address,birth_date,gender,credit,phone_numb) 
            VALUES(1,"Misha", "Solyan", "Borshchiv","1989-6-11", "male", 322, "+380686394800")""")
    c.commit()

cu.execute('SELECT sum(credit) FROM user')
for rec in cu.fetchall():
    print("Cума усіх кредитів:",rec[0], "UAH")
cu.execute('SELECT max(birth_date),name,surname FROM user')
for rec in cu.fetchall():
    print("Наймолодший кредитор:",rec)
cu.execute('SELECT * FROM user')
for rec in cu.fetchall():
    print(rec)
c.close()
