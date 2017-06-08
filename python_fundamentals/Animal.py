# Animal
class Animal(object):
    """docstring for Animal."""
    def __init__(self, name):
        # super(Animal, self).__init__()
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health: ", self.health
        return self
class Dog(Animal):
    """docstring for Dog."""
    def display_health(self):
        self.health = 150
        # super(Dog, self).__init__()
        self.health += 5
        # pet: increases health by 5
        return self
class Dragon(Animal):
    """docstring for Dragon."""
    def display_health(self):
        # super(Dragon, self).__init__()
        self.health = 170
        print "I'm dragon", sef.health
        return self

animal1 = Animal("Animal_name")
animal1.walk().walk().walk().run().run().display_health()

# Dog walk() three times, run() twice, pet() once, and have it displayHealth().
dog1 = Animal("100")

# animal2 = Animal("Dragon")
# animal2.display_health()
