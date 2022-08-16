from operations import operation

class ListOperation(operation.Operation):
   def list_files(self):
      dropbox_file_path = ""
      file_name_list = []
      self.operation.users_get_current_account()
      files_list = self.operation.files_list_folder(dropbox_file_path).entries
      for file_name in files_list:
         file_name_list.append(file_name.name)
      return file_name_list