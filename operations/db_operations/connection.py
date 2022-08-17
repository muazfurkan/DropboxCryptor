import mysql.connector

class Connector:
   def __init__(self):
      self.db = mysql.connector.connect(
         # Bu 3 özellik yıldızla gösterilecek!
         host='localhost',
         user='****',
         passwd='****',
         database='****'
      )
      self.cursor = self.db.cursor()
