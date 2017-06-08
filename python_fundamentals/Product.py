class Product(object):
    """docstring for Product."""
    def __init__(self, Price, Item_Name, Weight, Brand, Cost, Status= "for sale"):
        # super(Product, self).__init__()
        self.Price = Price
        self.Item_Name = Item_Name
        self.Weight = Weight
        self.Brand = Brand
        self.Cost = Cost
        self.Status = Status
    def sell(self):
        self.Status = "Sold"
        return self
    def add_tax(self):
        tax = .09
        self.price = self.price + (self.price * tax)
        return self
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.Status = "defective"
            self.price = 0
            print self.price
            print self.Status
        elif    reason_for_return == "like_new":
            self.Status = "used"
            self.price = self.price * .80
            print self.price
            print self.Status
        return self
    def display_info(self):
        if self.Status == "defective":
            self.Status = "defective"
            self.price = 0
            print self.price
            print self.Status
        elif    reason_for_return == "like_new":
            self.Status = "used"
            self.price = self.price * .80
            print self.price
            print self.Status
        else:
            print "Price: $", self.Price
        print "Item_Name:", self.Item_Name
        print "Weight:", self.Weight
        print "Brand:", self.Brand
        print "Cost:", self.Cost
        print "Status:", self.Status
        return self

product1 = Product(100, "Item_Name", 10, "Brand", 10)

product1.return_item("defective").display_info()
