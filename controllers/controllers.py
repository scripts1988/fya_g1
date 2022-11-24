from ..models import employee as md
# from ..models import io as IOEmployee
# import csv

class Controller:

    # def __init__(self, model, view):
    #     self.model = model
    #     self.view = view

    def insert_e(self, name, dob, position):
        em = md.Employee
        em.create_employee(name, dob, position)

    def delete_e(self, name):
        em = md.Employee
        em.del_employee(name)
