from .connection import Connector
import hashlib

class DeleteItem:
   def __init__(self):
      self.connector = Connector()
      self.cursor = self.connector.db.cursor()

   def delete_item(self, selected_file_name):
      _hasher = hashlib.sha256()
      _selected_file = selected_file_name
      file_name_hash = _hasher.update(_selected_file.encode('utf-8'))
      sqlq_delete = "DELETE FROM File WHERE fileName=(%s) AND fileHash=(%s)"
      self.cursor.execute(sqlq_delete, (_selected_file, file_name_hash))
      self.connector.db.commit()