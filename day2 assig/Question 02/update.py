# import mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb"
    )

def update_employees(empid, sallary):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update employees SET sallary = %s where empid = %s;"
    val = (sallary, empid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_employees(48,60000)












