'''

import mysql.connector

   *** CONNECT DATA BASE ***

db = mysql.connector.connect(
   host='localhost',    -->   Host type
   user='****',         -->   User name
   passwd='****',       -->   User password
   database='****'      -->   Database name
)

mycursor = db.cursor()


            *** CREATE DATABASE ****
   
      mycursor.execute("CREATE DATABASE DropboxDB")
      mycursor.execute("CREATE TABLE Account (id int PRIMARY KEY AUTO_INCREMENT, appKeys VARCHAR(50))")
      mycursor.execute("CREATE TABLE File (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Account(id), fileName VARCHAR(64), aesKey VARCHAR(64), fileHash VARCHAR(64))")

'''

