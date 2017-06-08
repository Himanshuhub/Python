class Bike(object):
    """docstring for Bike."""
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "30mph")
bike3 = Bike(300, "40mph")



# create 3 instances of the bike class
'''
'''
class Bike(object):

    def __init__(self,price,max_speed,miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles =miles
    def displayInfo(self):
        print self.price,self.max_speed,self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles = self.miles+10
        return self
    def reverse(self):
        print "Reversing"
        self.miles = self.miles-5
        if(self.miles<0):
            self.miles =0
        return self


bike1 = Bike(200,"25mph")
bike2 = Bike(300,"30mph")
bike3 = Bike(400,"50mph")
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
