class person:
    def __init__(self, firstName,lastName):
       self.firstName = firstName
       self.lastName = lastName
    def __str__(self):
        return f"{self.firstName}\t{self.lastName}"
    

class student(person):
    def __init__(self, firstName, lastName , year):
        super().__init__(firstName, lastName)
        self.year = year
    def __str__(self):
        return f'my name is {self.firstName} and i am born in {self.year}'

s = student('waseem','akram',2001)
print(s)