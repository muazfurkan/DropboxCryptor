from operations import operation, file_operations, output_directory
from tkinter import messagebox
from ..db_operations.connection import Connector
import hashlib

class FileDownload(operation.Operation):
   def download_file(self, selected_file, app_keys):
      file_operation = file_operations.FileOperations()
      selected_file_path = '/{0}'.format(selected_file)
      if selected_file == '':
         messagebox.showerror(title='No File Selected',
                              message='Select File From File List')
      else:
         connector = Connector()
         cursor = connector.db.cursor()
         file_name_hash = str(hashlib.sha256(selected_file.encode('utf-8')).hexdigest())
         sql_query_acc = "SELECT id FROM account WHERE appKeys = (%s)"
         sql_query_key = "SELECT aesKey FROM file WHERE userId = (%s) AND fileName = (%s)"
         sql_query_hash = "SELECT fileHash FROM file WHERE fileName = (%s)"
         cursor.execute(sql_query_acc, (app_keys,))
         for item in cursor:
            user_id = item[0]
            cursor.execute(sql_query_key, (user_id, file_name_hash))
            for key in cursor:
               self.aes_key = key[0]
         selected_local_path = file_operation.select_directory() + selected_file_path
         self.operation.files_download_to_file(selected_local_path, selected_file_path)
         file_operation.decryption(selected_local_path, self.aes_key)
         downloaded_file_path = output_directory.Output(selected_local_path).create_output_path('.dec')[0]
         file_hash = file_operation.hash_file(downloaded_file_path)
         cursor.execute(sql_query_hash, (file_name_hash,))
         for hash in cursor:
            self.db_file_hash = hash[0]
         if file_hash == self.db_file_hash:
            messagebox.showinfo(title='',
                                message='File is Secure!')
         else:
            file_operation.delete_file(downloaded_file_path)
            messagebox.showerror(title='',
                                 message='Dangerous File Deleted')
