from .connection import Connector
import hashlib

class AddItems:
   def __init__(self, app_keys):
      self.connector = Connector()
      self.cursor = self.connector.db.cursor()
      self.app_keys = app_keys
      self.cursor.execute("SELECT * FROM account")
      self.key_check = False
      for item in self.cursor:
         if item[1] == self.app_keys:
            self.key_check = True

   def add_items(self, file_name, aes_key, file_hash):
      _file_name_hash = hashlib.sha256(file_name.encode('utf-8')).hexdigest()
      if self.key_check == False:
         self.cursor.execute("INSERT INTO account (appKeys) VALUES (%s)", (self.app_keys,))
         _sqlq_insert = "INSERT INTO File (userId, fileName, aesKey, fileHash) VALUES (%s,%s,%s,%s)"
         _last_id = self.cursor.lastrowid
         self.cursor.execute(_sqlq_insert, (_last_id, _file_name_hash, aes_key, file_hash))
         self.connector.db.commit()
      else:
         _sqlq_insert = "INSERT INTO File (userId, fileName, aesKey, fileHash) VALUES (%s,%s,%s,%s)"
         _sqlq_acc = "SELECT appKeys FROM account WHERE appKeys = (%s)"
         self.cursor.execute(_sqlq_acc, (self.app_keys))
         for item in self.cursor:
            _acc_id = item[0]
            self.cursor.execute(_sqlq_insert, (_acc_id, _file_name_hash, aes_key, file_hash))
         self.connector.db.commit()