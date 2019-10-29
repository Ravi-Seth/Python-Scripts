class Vehicle :
    def __init__(self,name,speed,wheels):
        self.name=name
        self.speed=speed
        self.wheels=wheels

    def Vehicle_display(self):
        print ("%s is of speed %d and has Wheels %d" %(self.name,self.speed,self.wheels))

class car(Vehicle):
    def __init__(self,name,speed,wheels,brand):
        super().__init__(self,name,speed,wheels)
        self.brand=brand

    def car_display(self):
        print ("%s is of speed %d and has Wheels %d and brand %s" %(self.name,self.speed,self.wheels,self.brand))



v1=Vehicle("Bus",20,6)
v1.Vehicle_display()

c1=car("Wagon R",50,4,"Maruti")
c1.car_display()
