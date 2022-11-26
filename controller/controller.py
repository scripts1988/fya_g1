from models import IOEmployeeFile, Employee


class Controller:
    def __init__(self, employeeList, io, max_employee):
        self._employeeList = employeeList
        self._io = io
        self._max_employee = max_employee

    # Return list
    def search(self, nameToFind):
        result = []
        for employee in self._employeeList:
            name = Employee.get_name(employee)
            if (nameToFind == name):
                result.append(employee)
        return result

    def modify(self, id, newName, newDob, newPosition):
        self._employeeList[id].set_information(newName, newDob, newPosition)
        # for employee in self._employeeList:
        #     name = Employee.get_name(employee)
        #     if (nameToModify == name):
        #         employee.set_information(newName, newDob, newPosition)

    def add(self, name, dob, position):
        if len(self._employeeList) < self._max_employee:
            result = Employee()
            result.set_information(name, dob, position)
            self._employeeList.append(result)

    def delete(self, id):
        # for employee in self._employeeList:
        #     name = Employee.get_name(employee)
        #     if (nameToDelete == name):
        #         self._employeeList.remove(employee)

        self._employeeList = self._employeeList[:id] + self._employeeList[id+1:]

    def getEmployeeList(self):
        return self._employeeList

    def saveData(self):
        self._io.write_employees_to_file(self._employeeList)