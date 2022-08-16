from operations import operation, file_operations
from operations.db_operations import add_items

class Upload(operation.Operation):
   def upload_file(self):
      file_operation = file_operations.FileOperations()
      selected_file = file_operation.select_file()
      self.encrypted_file = file_operation.encryption(selected_file)
      _encrypted_file = self.encrypted_file[0]
      self.file_name = self.encrypted_file[1]
      dropbox_path = '/{0}'.format(self.file_name)
      self.file_hash = file_operation.hash_file(selected_file)
      with open(_encrypted_file, 'rb') as file:
         self.operation.files_upload(file.read(), dropbox_path, mute=True)

   def upload_items_database(self, app_keys):
      add_object = add_items.AddItems(app_keys)
      add_object.add_items(self.file_name, self.encrypted_file[2], self.file_hash)