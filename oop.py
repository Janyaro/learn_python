# class car:
#     x = 5
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#         # this method is used when the used just print an object instead of call the variable of the objects
#     def __str__(self):
#         return f"my name is {self.name} and i am show when the use just want to print an object"

# p = car('Waseem' ,"12")
# print(p)
# print(p.name)
# print(p.age)

class mycar:
    num1 = 23
    def __init__(self , name,age ,num):
     self.name = name
     self.age = age
     self.num = num
    def __str__(self):
       return f"{self.name} and age is {self.age}"
    def ageController(self):
       if 12 == self.num:
         print('jhell')
       else:
          print('my words')
p = mycar('waseem',23,53)
p.ageController()
print(p.name)
# to delete the property of an object inside the class you use the 'del' keyword but you can access that variable  through the class name and same thing will used to delete the class 
del mycar.num1
#if your method is empty and doesnot contain any defination then you can write the 'pass' in that method body to avoid the error 
# def myfunc():
#    pass
# print(p.num1)
