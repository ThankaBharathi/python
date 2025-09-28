
'''
name = "thanka"
age = 21
print(name.upper())
print(type(age))


class Dog:  # creating a dog class
    def bark(self):
        print("Whoof Whoof")

dog1 = Dog()  # dog object 
dog1.bark()



class Human:
    Name = None
    Age = None
    Weight = None
    Height = None
    
    def sleep(self):
        print(self.Name + " is sleeping")
    
person = Human()

person.Name = "Thanka"
person.Age = 21
person.Weight = 5
person.Height = 12

print(person.Name)
print(person.Height)

person.sleep()
'''

# Objects are have two things state and behavior
# state means creating a object and initializes a values
# Behaviour means creating a function for that class as a behaviour and class that 
 
 
class Student:
    RegNo = None
    Tamil = None
    English = None
    Math = None
    Sci = None
    Soc = None
    
    def marks(self):
        print(self.Tamil + self.English + self.Math + self.Sci + self.Soc ,"/ 500")
    
    

student1 = Student()
student1.RegNo = 1
student1.Tamil = 90
student1.English = 90
student1.Math = 86
student1.Sci = 99
student1.Soc = 98

student2 = Student()
student2.RegNo = 2
student2.Tamil = 87
student2.English = 90
student2.Math = 90
student2.Sci = 98
student2.Soc = 98


student3 = Student()
student3.RegNo = 3
student3.Tamil = 99
student3.English = 98
student3.Math = 97
student3.Sci = 95
student3.Soc = 98

student4 = Student()
student4.RegNo = 4
student4.Tamil = 80
student4.English = 90
student4.Math = 98
student4.Sci = 91
student4.Soc = 88

student5 = Student()
student5.RegNo = 5
student5.Tamil = 99
student5.English = 99
student5.Math = 99
student5.Sci = 98
student5.Soc = 98

student6 = Student()
student6.RegNo = 6
student6.Tamil = 50
student6.English = 30
student6.Math = 23
student6.Sci = 78
student6.Soc = 55

student7 = Student()
student7.RegNo = 7
student7.Tamil = 88
student7.English = 55
student7.Math = 89
student7.Sci = 45
student7.Soc = 67

student8 = Student()
student8.RegNo = 8
student8.Tamil = 99
student8.English = 100
student8.Math = 100
student8.Sci = 100
student8.Soc = 100

student9 = Student()
student9.RegNo = 9
student9.Tamil = 88
student9.English = 72
student9.Math = 76
student9.Sci = 87
student9.Soc = 96

student10 = Student()
student10.RegNo = 10
student10.Tamil = 77
student10.English =90
student10.Math = 98
student10.Sci = 66
student10.Soc = 84

print(student1.RegNo)
print(student1.marks())

