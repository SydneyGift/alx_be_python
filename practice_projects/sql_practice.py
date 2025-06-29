import mysql.connector
#Create the database
mydb = mysql.connector.connect(
    host="localhost",
    user="Syd",
    password="Pass",
    database="mydb"
)

mycursor = mydb.cursor()

#Creating a  table named customers if it does not exist yet

mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
)
""")

#Confirm if table has successfully been created
print("Table created successfully!")

#Insertng some customer data intyo the database
sql = "INSET INTO customers (name, email) VALUES (%s, %s)"
val = ("John Doe", "john.doe@example.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) iserted")

#read all customer data within the database
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

print("Customers:")
for row in myresult:
    print(row)