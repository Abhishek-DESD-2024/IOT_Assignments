import emp_dbconn

def update_employee(empid, salary):

    conn = emp_dbconn.get_connection()

    query = f"update employee SET salary = %s where empid = %s;"
    val = (salary,empid)

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()

update_employee(456,80000)