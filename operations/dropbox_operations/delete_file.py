from operations import operation
from tkinter import messagebox
from operations.db_operations import delete_item

class Delete(operation.Operation):
   def delete_file(self, selected_file):
      self.selected_file = selected_file
      selected_file_path = '/{0}'.format(self.selected_file)
      if self.selected_file == '':
         messagebox.showerror(title='No File Selected',
                              message='Select File From File List')
      else:
         self.operation.files_delete_v2(selected_file_path)
         messagebox.showerror(title='',
                              message='File is Deleted')

   def delete_item_database(self):
      delete_object = delete_item.DeleteItem()
      delete_object.delete_item(self.selected_file)