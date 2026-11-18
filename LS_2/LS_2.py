class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def drive_to(self,city):
        print(f"Car model: {self.model} driving to {city}")

    def color_change(self,new_color):
        self.color = new_color
        print(f"Car model:{self.model} changed color to {self.color}")


# Можем переопредеить методы
class Bus(Car):
    def __init__(self,color,model,number):
        super().__init__(color,model)
        self.number = number

    def drive_to(self,city):
        super().drive_to(city)
        print(f"Автобус {self.model} едет в {city}")


class Truck(Car):
    def drive_to(self,city):
        print(f"Truck model: {self.model} driving to {city}")





car1 = Car("Blue","BMW")
car1.drive_to("Manas")
car1.color_change("Black")
print(car1.color)


bus1 = Bus("Red","Kamaz","55")
print(bus1.color)
print(bus1.model)
bus1.color_change("Violet")
print(bus1.color)
bus1.drive_to("Naryn")


truck = Truck("Black","Hyundai")
truck.drive_to("Osh")


