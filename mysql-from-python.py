import os
import pymysql

#Get username from workspace
username = os.getenv('C9_USER')

#connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        #Read a single record
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close connection
    connection.close()