import mysql.connector
from mysql.connector import Error

try:
    print("Establishing Connection")
    connection = mysql.connector.connect(host='localhost',
                                         database='mockdatabase',
                                         user='root',
                                         password='root')
    print("Connection Established")

    print("executing select query")
    mySql_select_Query = "select * from appliances"
    print("select query executed")
    cursor = connection.cursor(buffered=True)
    print("cursor generated")
    cursor.execute(mySql_select_Query)
    print("select query executing")
    records = cursor.fetchall()

    print("Total number of rows is: ",cursor.rowcount)

    print("Sr\tDevice Name\tDevice Status\tTime Triggered")

    for row in records:
        print(row[0],"\t",row[1],"\t\t",row[2],"\t\t",row[3],"\t\t")
    
except Error as e:
    print("Error while connecting to MySQL",e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection is closed")
