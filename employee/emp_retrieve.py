import emp_dbconn

def retrieve_employee():

    conn = emp_dbconn.get_connection()

    query1 = "select * from employee;"
    query2 = f"select * from employee where department = 'dhjg';"
    query3 = f"select * from employee order by salary DESC LIMIT 1;"
    query4 = f"select * from employee order by salary ASC LIMIT 1;"

    cursor = conn.cursor()
    cursor.execute(query1)
    records = cursor.fetchall()
    print("All employees details")
    for value in records:
        print(value)
    print()
    cursor.close()
     
    cursor = conn.cursor()
    cursor.execute(query2)
    records = cursor.fetchall()
    print("Employees of given department")
    print(records)
    print( )
    cursor.close()

    cursor = conn.cursor()
    cursor.execute(query3)
    records = cursor.fetchall()
    print("Employee with highest and lowest salary")
    print(records)   
    cursor.close()

    cursor = conn.cursor()
    cursor.execute(query4)
    records = cursor.fetchall()
    print(records)
    print( )
    cursor.close()
    
    conn.close()

retrieve_employee()