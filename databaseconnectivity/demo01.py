import mysql
import mysql.connector as db
# root@localhost:3306
# jdbc:mysql://localhost:3306/?user=root
url = "localhost"
user = "root"
password = "Demo@123"
schema = "sbi_db"


def insertData(id,name,contact,address):
        try:
            connection = db.connect(host=url, user=user, password=password, database=schema)
            if (connection.is_connected()):
                print("db connected successfully")
            cursor = connection.cursor()
            cursor.execute("insert into bank (bank_id,name,contact,address) values ("+str(id)+",'"+name+"','"+contact+"','"+address+"')")
            connection.commit()
        except mysql.connector.Error as err:
            print(err)


def updateData():
        try:
            connection = db.connect(host=url, user=user, password=password, database=schema)
            if (connection.is_connected()):
                print("db connected successfully")
            cursor = connection.cursor()
            cursor.execute("update bank set contact='151212323' where bank_id=101")
            connection.commit()
        except mysql.connector.Error as err:
            print(err)


def deleteData():
    try:
        connection = db.connect(host=url, user=user, password=password, database=schema)
        if (connection.is_connected()):
            print("db connected successfully")
        cursor = connection.cursor()
        cursor.execute("delete from bank where bank_id=100")
        connection.commit()
    except mysql.connector.Error as err:
        print(err)


insertData(102,"SBI","56124545","Mumbai")


