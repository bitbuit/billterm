import json
import os.path
import os

# -- Key/Value style memory/store(json) DB
class Json_db(object):
 
  def __init__(self, filename):
    self.filename = filename
    self.__memory = {}
    if os.path.isfile(self.filename):
      with open(self.filename) as json_file: 
        self.__memory = json.load(json_file)

  def set(self, key, value):
    self.__memory[key] = value
 
  def get(self, key):
    return self.__memory[key]
  
  def exists(self, key):
    return key in self.__memory

  def keys(self, sort='asc'):
    return sorted(self.__memory.keys(), reverse=(sort == 'desc'))
 
  def store(self):
    with open(self.filename, 'w') as outfile: 
      json.dump(self.__memory, outfile, indent=4)   

