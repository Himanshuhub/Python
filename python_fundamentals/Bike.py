class Bike(object):
    """docstring for Bike."""
    def __init__(self, price, max_speed, miles=0):
        # super(Bike, self).__init__()
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Bike info: Price $", self.price, " Maximum Speed: ", self.max_speed, "MPH Miles: ", self.miles
        return self
    def ride(self):
        print "Riding: "
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing", self.miles - 5
        if self.miles < 0:
            self.miles = 0
        self.miles -= 5
        return self

bike1 = Bike(1000, 25, 0)
bike2 = Bike(500, 20, 1000)
bike3 = Bike(700, 25, 20)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo
