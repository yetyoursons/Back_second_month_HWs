
import sqlite3
database = sqlite3.connect("notes_user.db")
sql = database.cursor()

# sql.execute(
#     """
#     CREATE TABLE schedule(
#     person TEXT,
#     day TEXT,
#     time TEXT,
#     to_do TEXT
#     )
#     """
# )
#
# database.commit()
def task():
    global person, day, time, to_do
    person = input("Введите имя:")
    day = input("Введите день недели:")
    time = input("Введите время:")
    to_do = input("Что надо сделать?")

    sql.execute(f"SELECT to_do FROM schedule WHERE to_do = '{to_do}' ")

    if sql.fetchone() is None:
        #execute приводит курсор в исполнение
        sql.execute(f"INSERT INTO schedule VALUES (?, ?, ?, ?)",(person,day,time,to_do))
        database.commit()
        print("Дело записано!")

    else:
        print("Дело уже записано")
        for value in sql.execute("SELECT*FROM schedule"):
            print(value)

task()