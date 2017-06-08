class Car(object):
    """docstring for Car."""
    def __init__(self, price, speed, fuel, mileage, tax=.12):
        # super(Car, self).__init__()
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def DisplayAll(self):
        print "Price: $", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage,"mpg"
        print "Tax:", self.tax

car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Not Full", 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(20000, 35, "Full", 15)

car1.DisplayAll()
car2.DisplayAll()
car3.DisplayAll()
car4.DisplayAll()
car5.DisplayAll()
car6.DisplayAll()
