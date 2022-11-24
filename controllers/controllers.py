from models.employee import Employee

class Controller:

    def __init__(self):
        self.employeeList = []

    def search_e(self, name):
        for e in self.employeeList:
            if(e.name == name):
                return True
        
        return False

    def insert_e(self, name, dob, position):
        if (self.search_e(name)):
            return False
        else:
            newEmployee = Employee() 
            newEmployee.set_information(name, dob, position)
            self.employeeList.append(newEmployee)
            return True

    def delete_e(self, name):
        if(self.search_e(name)):
            for em in self.employeeList:
                if(em.name == name):
                    self.employeeList.remove(em)
           
        else:
            return False