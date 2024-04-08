# Class definition
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
    
    def description(self):
        print(self.name)
        print(self.age)
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_hungry, giraffe.is_alive)
print(panda.name, panda.age, panda.is_hungry, panda.is_alive)

hippo = Animal("hippo", 2, False)
hippo.description()

sloth = Animal("sloth", 1, True)
ocelot = Animal("ocelot", 4, False)

print(hippo.health)
print(sloth.health)
print(ocelot.health)