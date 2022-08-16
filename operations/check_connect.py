import dropbox
from windows import dropbox_window
from tkinter import messagebox
from operations import operation

class Connection(operation.Operation):
   def check_token(self, token, app_key):
      _token = token.strip()
      try:
         oauth_result = self.operation.finish(_token)
         access_token = oauth_result.access_token
         connect_dropbox = self.connect_dropbox(oauth_result)
         # self.connect_database()
         messagebox.showinfo(title='',
                             message='Connection Successfully Established')

      except Exception as exception:
         messagebox.showerror(title='Connection Failed',
                              message='            '
                                      'Try Again!'
                                      '            ')
      else:
         _dropbox_window = dropbox_window.DropboxWindow(650, 450, 'Dropbox')
         _dropbox_window.set_window(self.dbx, app_key)

   def connect_dropbox(self, oauth_result):
      with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as self.dbx:
         self.dbx.users_get_current_account()
