import mysql.connector

class DBConnect:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def insertData(self, account_number, name, password, email, account_type, address):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO users (account_number, name, password, email, Account_type, address) VALUES (%s, %s, %s, %s, %s, %s)"

        val = (account_number, name, password, email, account_type, address)

        mycursor.execute(sql, val)
        self.mydb.commit()
