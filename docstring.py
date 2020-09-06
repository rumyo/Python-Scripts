class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)

'''
Here is your output:
Help on class Person in module submission:

class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  greeting(self)
 |      Outputs a message with the name of the person
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 
 '''
