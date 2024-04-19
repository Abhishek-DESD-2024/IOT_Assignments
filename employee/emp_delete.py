import emp_dbconn

def delete_employee(empid):

    conn = emp_dbconn.get_connection()

    query = f"delete from employee where empid = %s;"
    val = (empid,)

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()

delete_employee(123)