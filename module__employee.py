class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def give_raise(self, increase=5000):
        self.salary += increase