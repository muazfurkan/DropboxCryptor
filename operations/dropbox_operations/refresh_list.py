from operations import operation
from operations.dropbox_operations import list_files

class List(operation.Operation):
   def upload_list(self):
      get_dropbox_files = list_files.ListOperation(self.operation)
      dropbox_files_list = get_dropbox_files.list_files()
      return dropbox_files_list