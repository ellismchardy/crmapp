import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Weepatsy1064'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE emdevcrm")

print('Database created...')
