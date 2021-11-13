class Employee():

    def __init__(self, id, name, location_id):
        self.id = id
        self.name = name
        self.location_id = location_id
        self.location = None
        
#new_employee = Employee(1, "Chris Barker", 3)