class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vInstance1=Vehicle(100,20.55)
print(vInstance1.max_speed,vInstance1.mileage)