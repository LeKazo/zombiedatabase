#myfile = open("data.txt", "w+")
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="E0095CAa12#" database="zombieinfo")
cursor = mydb.cursor()

while(True):

uName = input("enter Zombie Name")

if uName =='quit':
    exit()



uAge = input("Enter Zombie Age")
uType = input("Enter Ctype of zombie")

sql = "INSERT INTO zombies (name, age, type) VALUES (%s, %s, )"
vals = (uName, uAge, uType)
cursor.execute()
mydb.commit()
#myfile.write("\r\n zombie name: "+uName+"\r\n")
#myfile.write("zombie age: "+uAge+" \r\n")
#myfile.write("type of zombie: "+uType+" \r\n")
print("\r\n data saved to the database \r\n")
