import customtkinter

class Window:
   def __init__(self, height, width, window_title):
      self.height = int(height)
      self.width = int(width)
      self.window_title = window_title
      self.entry_list = []
      customtkinter.set_appearance_mode('dark')
      customtkinter.set_default_color_theme('dark-blue')

   def get_entry(self, box_name):
      entry = box_name.get()
      self.entry_list.append(entry)
      return self.entry_list

