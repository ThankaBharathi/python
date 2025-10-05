class Form:
    Name = None
    Age = None
    Gender = None
    Adress = None

xerox1 = Form()
xerox1.Name = "Thanka"
xerox1.Age = 21
xerox1.Gender = "Male"
xerox1.Adress = "1/51b, Bungalow street vilathikulam"

xerox2 = Form()
xerox2.Name = "Bharathi"
xerox2.Age = 20
xerox2.Gender = "Male"
xerox2.Adress = "1/51b, Bungalow street vilathikulam"

print(xerox1.Name)


class Human:
    def __init__(self,Color,Hight,Weight):
        self.Color = Color
        self.Hight = Hight
        self.Weight = Weight

thanka = Human("Orange",19.2,43)
print(thanka.Color)
