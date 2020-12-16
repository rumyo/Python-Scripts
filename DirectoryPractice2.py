import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  dir = os.getcwd()
  relative_parent = os.path.join(dir)

  # Return the absolute path of the parent directory
  return os.path.dirname(relative_parent)

print(parent_directory())

#output is: /
