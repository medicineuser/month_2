


class Car:
    def __init__(self,color,model,fined):
        self.color = color
        self.model = model
        self._fined = fined
        self.__max_speed = 100

    def _calculate_fuel(self):
        print(f"{self.model} charged fuel {self._fined}")
        return 0

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, new_max_speed):
        if 0 > new_max_speed or new_max_speed > 250:
            raise ValueError("Non realistic speed")
            return False
        self.__max_speed = new_max_speed



# property getter and setter

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self,new_max_speed):
        print("new setter changed max speed")
        if 0 > new_max_speed or new_max_speed > 250:
            raise ValueError("Non realistic speed")
            return False
        self.__max_speed = new_max_speed



    def drive_to(self,city):
        print(f"Max Speed: {self.__max_speed}")
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





car1 = Car("Blue","BMW", True)
car1.drive_to("Manas")
car1.color_change("Black")
print(car1.color)
car1._fined =  not True
car1.drive_to("Batken")

car1.get_max_speed()
print(car1.get_max_speed())
car1.set_max_speed(200)
print(car1.get_max_speed())


# property getter and setter
print(car1.max_speed)
car1.max_speed = 180
print(car1.max_speed)


