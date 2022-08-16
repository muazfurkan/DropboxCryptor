import os

class Output:
   def __init__(self, source_path):
      self.source_path = source_path

   def create_output_path(self, operation_name):
      file_name = os.path.basename(self.source_path)
      output_directory = os.path.dirname(self.source_path)
      output_path = output_directory + '/' + file_name + operation_name
      return output_path, output_directory, file_name
