from .window import Window
from operations import check_connect
import customtkinter

class TokenCheckWindow(Window):
   def set_window(self, auth_flow, app_key):
      token_window = customtkinter.CTkToplevel()
      token_window.title(self.window_title)
      token_window.geometry(f'{self.height}x{self.width}+{int((1800 - self.width) / 2)}+{int((800 - self.height))}')
      token_entry = customtkinter.CTkEntry(token_window,
                                           width=320,
                                           height=45,
                                           text_font=('corbel', 15),
                                           placeholder_text_color='#828282',
                                           placeholder_text='TOKEN')
      token_entry.place(x=65, y=45)
      check_button = customtkinter.CTkButton(master=token_window,
                                             text_font=('corbel', 13),
                                             width=250,
                                             height=35,
                                             text='Check',
                                             command=lambda: [check_connect.Connection(auth_flow).check_token(self.get_entry(token_entry)[0], app_key),
                                                              token_window.destroy()])
      check_button.place(x=100, y=120)
      token_window.mainloop()