import tkinter as tk
from .window import Window
from .token_check_window import TokenCheckWindow
from PIL import Image, ImageTk
import customtkinter
from operations import get_token, open_url

class LoginWindow(Window):
   def set_window(self):
      self.login_window = customtkinter.CTk()
      self.login_window.title(self.window_title)
      self.login_window.geometry(f'{self.height}x{self.width}+{int((1800-self.width)/2)}+{int((800-self.height))}')
      self.login_window.overrideredirect(True)

      image_login_window = Image.open("windows/dbx-logo.png")
      resized_image = image_login_window.resize((150, 150))
      render = ImageTk.PhotoImage(resized_image)
      image_label_login_window = customtkinter.CTkLabel(master=self.login_window,
                                                        image=render)
      image_label_login_window.image = render
      image_label_login_window.place(x=int((self.height - 140) / 2), y=int((self.width - 350) / 2))

      entry_box1 = customtkinter.CTkEntry(self.login_window,
                                          width=250,
                                          height=45,
                                          text_font=('corbel', 15),
                                          placeholder_text_color='#828282',
                                          placeholder_text='App key'
                                          )
      entry_box1.place(x=200, y=220)
      entry_box2 = customtkinter.CTkEntry(self.login_window,
                                          width=250,
                                          height=45,
                                          text_font=('corbel', 15),
                                          placeholder_text_color='#828282',
                                          placeholder_text='App secret'
                                          )
      entry_box2.place(x=200, y=275)
      login_button = customtkinter.CTkButton(master=self.login_window,
                                             text_font=('corbel', 13),
                                             width=170,
                                             height=35,
                                             text='LogIn',
                                             command=lambda: [self.set_url_label(get_token.create_token_link(self.get_entry(entry_box1)[0], self.get_entry(entry_box2)[1])[1]),
                                                              TokenCheckWindow(450, 200, 'Token Check').set_window(get_token.create_token_link(self.get_entry(entry_box1)[0],
                                                                                                                                               self.get_entry(entry_box2)[1])[0],
                                                                                                                   (self.get_entry(entry_box1)[0] + self.get_entry(entry_box2)[1]))]
                                             )
      login_button.place(x=130, y=370)
      exit_button = customtkinter.CTkButton(master=self.login_window,
                                            text_font=('corbel', 13),
                                            width=170,
                                            height=35,
                                            text='Exit',
                                            command=self.login_window.destroy)
      exit_button.place(x=350, y=370)
      self.login_window.mainloop()

   def set_url_label(self, label_text):
      _authorize_url = tk.Label(self.login_window,
                                background='#1a1a1a',
                                foreground='white',
                                text=label_text)
      _authorize_url.place(x=95, y=420)
      _authorize_url.bind("<Button-1>",
                          lambda e: open_url._open_url(label_text))