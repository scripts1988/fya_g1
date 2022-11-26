from models import IOEmployeeFile
from views import MainScreen
from controller import Controller
import configs as cfgs
def main():
    #Declare an IO
    io = IOEmployeeFile(cfgs.PATH_TO_DATA)

    #Always init the list first
    emp = io.read_employees_from_file()
    #Create a controller for function with input output
    ctrl = Controller(emp)
    main_screen = MainScreen(controller=ctrl)


if __name__ == '__main__':
    main()