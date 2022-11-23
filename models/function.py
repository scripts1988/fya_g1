from employee import *
import csv
from csv import writer

class function_employee:
    def search_employee(self, name):
        lines = list()
        with open('data.csv', 'r') as inp:

            for row in csv.reader(inp):
                lines.append(row)
                for line in row:
                    if line == name:
                       return True

            return False

    def add_employee(self, name, dob, position):

        if(self.search_employee(name) == True):
            print("Cannot add because user did exist")
        else:
            newEmployee = [name, dob, position]
            with open('data.csv', 'a', newline='') as output:
                writer_object = writer(output)
                writer_object.writerow(newEmployee)
            
                output.close()

    def delete_employee(self, name):
        if(self.search_employee(name) == False):
            print("Cannot delete because user doesnt exist")
        else:
            lines = list()
            with open('data.csv', 'r') as inp:
                for row in csv.reader(inp):
                    lines.append(row)
                    for line in row:
                        if line == name:
                            lines.remove(row)

            with open('data.csv', 'w', newline='') as output:
                writer_object = writer(output)
                writer_object.writerows(lines)
                output.close()

# Debug
if __name__ == '__main__':
    
    function = function_employee()
    function.add_employee("ABC", "34", "Firmware")
    function.add_employee("DEF", "12", "Algo")
    function.delete_employee("ABC")
