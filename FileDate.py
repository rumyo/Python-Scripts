import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename, "w") as f:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  newtime = datetime.date.fromtimestamp(timestamp)
  # Return just the date portion 
 
  return ("{}".format(newtime))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

#output is: 2020-12-16
