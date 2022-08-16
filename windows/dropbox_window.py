from tkinter import ANCHOR
import customtkinter
import tkinter as tk
from .window import Window
from PIL import Image, ImageTk
from operations.dropbox_operations import refresh_list
from operations import dbx_operation_object

class DropboxWindow(Window):
   def set_window(self, connection_refresh, app_key):
      self.dropbox_window = customtkinter.CTkToplevel()
      self.dropbox_window.title(self.window_title)
      self.dropbox_window.geometry(f'{self.height}x{self.width}+{int((1800-self.width)/2)}+{int((1000-self.height))}')
      # self.dropbox_window.overrideredirect(True)

      image_dropbox_window = Image.open("windows/dbx-logo.png")
      resized_image = image_dropbox_window.resize((125, 125))
      render = ImageTk.PhotoImage(resized_image)
      image_label_dropbox_window = customtkinter.CTkLabel(self.dropbox_window,
                                                          image=render)
      image_label_dropbox_window.image = render
      image_label_dropbox_window.place(x=int((self.height - 430) / 2), y=int((self.width - 396) / 2))

      refresh_file_list = refresh_list.List(connection_refresh)
      _refresh_file_list = refresh_file_list.upload_list()
      self.set_dropbox_file_list_box(_refresh_file_list)

      upload_button = customtkinter.CTkButton(master=self.dropbox_window,
                                              text_font=('corbel', 13),
                                              width=210,
                                              height=35,
                                              text='Upload File',
                                              command=lambda: [dbx_operation_object.CreateObject(connection_refresh).create_operation_object(app_keys=app_key, class_name='upload'),
                                                               self.set_dropbox_file_list_box(dbx_operation_object.CreateObject(connection_refresh).create_operation_object(class_name='list'))])
      upload_button.place(x=70, y=175)
      download_button = customtkinter.CTkButton(master=self.dropbox_window,
                                                text_font=('corbel', 13),
                                                width=210,
                                                height=35,
                                                text='Download File',
                                                command=lambda: [dbx_operation_object.CreateObject(connection_refresh).create_operation_object(app_keys=app_key, selected_file=self.get_selected_list_box_item(self.file_label),
                                                                                                                                                   class_name='download')])
      download_button.place(x=70, y=235)
      delete_button = customtkinter.CTkButton(master=self.dropbox_window,
                                              text_font=('corbel', 13),
                                              width=210,
                                              height=35,
                                              text='Delete File',
                                              command=lambda: [dbx_operation_object.CreateObject(connection_refresh).create_operation_object(app_keys=app_key, selected_file=self.get_selected_list_box_item(self.file_label),
                                                                                                                                                 class_name='delete'),
                                                               self.set_dropbox_file_list_box(dbx_operation_object.CreateObject(connection_refresh).create_operation_object(class_name='list'))])
      delete_button.place(x=70, y=295)
      exit_button = customtkinter.CTkButton(master=self.dropbox_window,
                                            text_font=('corbel', 13),
                                            width=300,
                                            height=35,
                                            text='Exit',
                                            command=self.dropbox_window.destroy)
      exit_button.place(x=175, y=380)
      self.dropbox_window.mainloop()

   def set_dropbox_file_list_box(self, label_text):
      self.file_label = tk.Listbox(self.dropbox_window,
                              background='#1a1a1a',
                              selectbackground='#5d5d5d',
                              foreground='white',
                              highlightthickness=0,
                              height=(11),
                              relief='flat',
                              font=('', 12),
                              listvariable=label_text
                              )
      for index, file in enumerate(label_text):
         self.file_label.insert(index, file)
      self.file_label.place(x=400, y=75)
      select_file_button = customtkinter.CTkButton(master=self.dropbox_window,
                                        text='Select File',
                                        text_font=('corbel', 13),
                                        width=20,
                                        command=lambda: self.get_selected_list_box_item(self.file_label))
      select_file_button.place(x=440, y=305)

   def get_selected_list_box_item(self, list_box_name):
      state = list_box_name.get(ANCHOR)
      return state