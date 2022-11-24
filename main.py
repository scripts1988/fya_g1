import sys
sys.path.append('models/')
sys.path.append('controller/')
from models.newIO import IOEmployeeFile
from models.employee import Employee
from controller import Controller

def main():
    #init an employee list
    emp = []
    #Declare an IO
    io = IOEmployeeFile()

    #Always init the list first
    emp = io.read_employees_from_file()

    #Create a controller for function with input output
    ctrl = Controller(emp)

    #Adding to the emp list first
    #a = ctrl.add('XYZ', '2002', 'KKK')
    #a = ctrl.add('JJJ', '2003', 'ZZZ')

    #If you want to modify something
    #a = ctrl.modify('XYZ', 'newName', '2001', 'modified')

    #If you want to delete
    a = ctrl.delete('Khang')

    #After doing all operation, save to file again
    io.write_employees_to_file(emp)
        

if __name__ == '__main__':
    main()