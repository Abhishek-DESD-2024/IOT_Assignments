import emp_dbconn

def add_person():

    conn = emp_dbconn.get_connection()

    empid = int(input("Enter empid : "))
    name = input("Enter name : ")
    department = input("Enter department : ")
    email = input ("Enter email: ")
    salary = int(input("Enter salary : "))
    date_of_joining = input ("Enter date_of_joining : ")

    query = f"insert into employee values({empid}, '{name}', '{department}','{email}',{salary},'{date_of_joining}');"

    cursor = conn.cursor()

    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()

add_person()