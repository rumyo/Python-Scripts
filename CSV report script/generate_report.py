#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True) #The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
        employee_list.append(data)
  return employee_list

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])

#We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.
  department_data = {}
  for department_name in set(department_list): #This uses the set() method, which converts iterable elements to distinct elements.
    department_data[department_name] = department_list.count(department_name)
  return department_data

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f: #the file mode is 'r' (reading) by default, so you should now explicitly pass 'w+' mode (open for reading and writing, overwriting a file) as a parameter.
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

employee_list = read_employees('/home/student-00-b44047602171/data/employees.csv')  #replace with csv file location
#print(employee_list)
dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, '/home/student-00-b44047602171/test_report.txt')
