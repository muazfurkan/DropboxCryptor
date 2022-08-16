from operations import operation
from operations.dropbox_operations import list_files, upload_crypted_file, download_decrypted_file, delete_file

class CreateObject(operation.Operation):
   def create_operation_object(self, app_keys='', selected_file='', class_name=''):
      if class_name == 'list':
         get_dropbox_files = list_files.ListOperation(self.operation)
         dropbox_files_list = get_dropbox_files.list_files()
         return dropbox_files_list
      elif class_name == 'upload':
         operation_upload_file = upload_crypted_file.Upload(self.operation)
         operation_upload_file.upload_file()
         operation_upload_file.upload_items_database(app_keys)
      elif class_name == 'download':
         operation_download_file = download_decrypted_file.FileDownload(self.operation)
         operation_download_file.download_file(selected_file, app_keys)
      elif class_name == 'delete':
         operation_delete_file = delete_file.Delete(self.operation)
         operation_delete_file.delete_file(selected_file)
         operation_delete_file.delete_item_database()