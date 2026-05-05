import mysql
import mysql.connector as db
# root@localhost:3306
# jdbc:mysql://localhost:3306/?user=root
url = "localhost"
user = "root"
password = "Demo@123"
schema = "sbi_db"

try:
    connection = db.connect(host=url,user =user,password=password,database=schema)
    if(connection.is_connected()):
        print("db connected successfully")
    cursor = connection.cursor()
    cursor.execute("insert into bank (bank_id,name,contact,address) values (100,'SBI',457845445,'Pune')")
    connection.commit()
except mysql.connector.Error as err:
    print(err)


