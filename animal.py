# Assignment: Animal

# Create an Animal class and give it the below attributes and methods. 
# Extend the Animal class to two child classes, Dog and Dragon.

# Objective
# The objective of this assignment is to help you understand inheritance. 
# Remember that a class is more than just a collection of properties and methods. 
# If you want to create a new class with attributes and methods that are already defined in another class, 
# you can have this new class inherit from that other class (called the parent) instead of copying and pasting code 
# from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods 
# of its own, for child instances to call. 
# 
# As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes 
# that inherit from the same parent class.

# Animal Class
# Attributes:
    #  name
    #  health
# Methods:
    # walk: decreases health by one
    # run: health decreases by five
    # display health: print to the terminal the animal's health.

# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() 
# to confirm that the health attribute has changed.


# Dog Class
#  inherits everything from Animal
# Attributes:
#  default health of 150
# Methods:
#  pet: increases health by 5

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().


# Dragon Class
#  inherits everything from Animal
# Attributes:
#  default health of 170
# Methods:
#  fly: decreases health by 10
#  display health: prints health by calling the parent method and prints "I am a Dragon"

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().

class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1    
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        return self

class dragon(animal): #dragon class inherits all from animal.
    def __init__(self,name,health): #still needs its own init
        super(dragon, self).__init__(name, health) #call the parent's init with the variables collected at creation.
        self.health = 170
    def fly():
        self.health -= 10
    def display_health(self):
        super(dragon, self).display_health()#call the parent's display_health, no params needed.
        print 'I am a Dragon' #in addition, dragon's display health prints "i am a dragon"
class dog(animal):
    def __init__(self,name,health):
        super(dog, self).__init__(name, health)   
        self.health = 150
    def pet(self):
        self.health += 5
        return self


# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, 
# and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().
generic_animal = animal('max', 10)
#generic_animal.fly()
generic_animal.display_health()
rex = dragon('rex',100)
rex.display_health()


ruby = dog('ruby', 10)
#ruby.fly()
#generic_animal().walk().walk().run().run().display_health()

#Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
#ruby.walk().walk().walk().run().run().pet().display_health()





