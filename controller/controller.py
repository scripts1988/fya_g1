import sys
sys.path.append('models/')
from models.newIO import IOEmployeeFile
from models.employee import Employee


class Controller:
    def __init__(self, employeeList):
        self._employeeList = employeeList

    def search(self, nameToFind):
        result = Employee()
        for employee in self._employeeList:
            name = Employee.get_name(employee)
            if (nameToFind == name):
                result = employee
        return result

    def modify(self, nameToModify, newName, newDob, newPosition):
        result = Employee()
        newIO = IOEmployeeFile
        for employee in self._employeeList:
            name = Employee.get_name(employee)
            if (nameToModify == name):
                employee.set_information(newName, newDob, newPosition)

    def add(self, name, dob, position):
        result = Employee()
        result.set_information(name, dob, position)
        self._employeeList.append(result)

    def delete(self, nameToDelete):
        for employee in self._employeeList:
            name = Employee.get_name(employee)
            if (nameToDelete == name):
                self._employeeList.remove(employee)

