from tkinter import filedialog
from operations import output_directory
import pyAesCrypt
import hashlib
import random
import string
import os

class RandomKey:
   def create_random_key(self):
      random_chars = ''.join(random.choice(string.printable) for i in range(100))
      hashed_chars = hashlib.sha256(random_chars.encode('utf-8')).hexdigest()
      return hashed_chars

class FileOperations:
   def select_file(self):
      self.source_path = filedialog.askopenfilename()
      return self.source_path

   def select_directory(self):
      self.output_directory = filedialog.askdirectory()
      return self.output_directory

   def encryption(self, source_path):
      _key = RandomKey()
      _aes_key = _key.create_random_key()
      path_object = output_directory.Output(source_path)
      output_path = path_object.create_output_path('.enc')
      _output_path = output_path[0]
      _output_directory = output_path[1]
      file_name = output_path[2]
      pyAesCrypt.encryptFile(source_path,
                             _output_path,
                             _aes_key)
      return _output_path, file_name, _aes_key

   def decryption(self, source_path, aes_key):
      path_object = output_directory.Output(source_path)
      output_path = path_object.create_output_path('.dec')
      _output_path = output_path[0]
      _output_directory = output_path[1]
      pyAesCrypt.decryptFile(source_path,
                             _output_path,
                             aes_key)

   def delete_file(self, source_path):
      os.remove(source_path)

   def hash_file(self, source_path):
      with open(source_path, 'rb') as file:
         hash_bytes = file.read()
         hash256 = hashlib.sha256(hash_bytes).hexdigest()
      return hash256


