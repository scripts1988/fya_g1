class Employee:
    def __init__(self,name=None,dob=None, position=None):
        self._name = name
        self._dob = dob
        self._position = position

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def get_position(self):
        return self._position

    def set_name(self, name):
        self._name = name
    
    def set_dob(self, dob):
        self._dob = dob
    
    def set_position(self, position):
        self._position = position

    def set_information(self, name,dob, position):
        self._name = name
        self._dob = dob
        self._position = position

    def get_information(self):
        return {
            'name': self._name,
            'DoB': self._dob,
            'position': self._position
        }
    def __str__(self):
        return str(self.get_information())
    
    def format_csv(self):
        return "%s,%s,%s\n" % (self._name, self._dob, self._position)
