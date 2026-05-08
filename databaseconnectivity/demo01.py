import mysql
import mysql.connector as db
# root@localhost:3306
# jdbc:mysql://localhost:3306/?user=root
url = "localhost"
user = "root"
password = "Demo@123"
schema = "sbi_db"

class Bank:
    def __init__(self):
        self.name= None
        self.id = None
        self.contact = None
        self.address = None

    def __init__(self,id,name,contact,address):
        self.name = name
        self.id = id
        self.contact = contact
        self.address = address

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


def updateData(bank):
        if(isinstance(bank,Bank) == False):
            return
        query = ""
        if (bank.contact != None and bank.address != None and bank.name != None):
            query = "update bank set name='" + bank.name + "', contact='" + bank.contact + "',address='" + bank.address + "' where bank_id=" + str(bank.id)
        elif (bank.name != None and bank.contact != None):
            query = "update bank set name='" + bank.name + "',contact='" + bank.contact + "' where bank_id=" +str(bank.id)
        elif (bank.name != None and bank.address != None):
            query = "update bank set name='" + bank.name + "',address='" + bank.address + "' where bank_id=" + str(bank.id)
        elif (bank.contact != None and bank.address != None):
            query = "update bank set contact='" + bank.contact + "',address='" + bank.address + "' where bank_id=" + str(bank.id)
        elif(bank.address != None):
            query = "update bank set address='"+bank.address+"' where bank_id="+str(bank.id)
        elif(bank.contact != None):
            query = "update bank set contact='"+bank.contact+"' where bank_id="+str(bank.id)
        elif(bank.name != None):
            query = "update bank set name='"+bank.name+"' where bank_id="+str(bank.id)

        try:
            connection = db.connect(host=url, user=user, password=password, database=schema)
            if (connection.is_connected()):
                print("db connected successfully")
            cursor = connection.cursor()
            cursor.execute(query)
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


# insertData(102,"SBI","56124545","Mumbai")
print(type(Bank(102,"RBI","665656565","nagpur")))
updateData(Bank(102,"RBI","665656565","nagpur"))

