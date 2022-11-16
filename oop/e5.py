class Vehicle:

    def __init__(self, name, max_speed, mileage,color):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

color="white"
school_bus = Bus("school bus",100,20.55,color)
personal_car = Car("merc",200,16.77,color)

print(school_bus.color)
print(personal_car.color)