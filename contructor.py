class Employee:
    no_of_leaves = 0

    def __init__(self, name, salary, role):  #argument
        self.name = name      #instance variable
        self.salary = salary
        self.role = role

    def printdetails(self):   #Self means the object which we are talking
        return {self.name}


feroz = Employee("Feroz", 100000, "Instructor")
print(feroz.printdetails())



