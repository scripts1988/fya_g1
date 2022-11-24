from .employee import Employee

class IOEmployeeFile:
    def __init__(self,path='.data.csv') -> None:
        self._path = path
        self._header = 'name,dob,position'
        assert path[-4:] == '.csv', 'Invalid format file'

    def read_employees_from_file(self):
        with open(self._path, 'r') as r:
            lines = r.read().splitlines()
            # print(lines)
            # header = lines[0].split(',')
            assert lines[0] == self._header, 'Error header'

            employees = []
            for line in lines[1:]:
                name, dob, position = line.split(',')
                employees.append(Employee(name, dob, position))

            r.close()
            return employees

    def write_employees_to_file(self, employees):
        with open(self._path, 'w') as w:
            w.writelines(self._header)
            w.writelines('\n')
            for em in employees:
                w.writelines(em.format_csv())
            w.close()



# Debug
if __name__ == '__main__':
    
    data = [Employee('A', 'B', 'C')]
    io = IOEmployeeFile()
    # io.write_employees_to_file(data)
    em = io.read_employees_from_file()
    print(em[0])

