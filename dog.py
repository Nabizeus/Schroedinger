class Dog:

    species = "Canis familiaris"

    def __init__(self,name, age):

        self.name = name
        self.age = age
        #self.breed = breed integrated as Child Class

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound='Arfx'):
        return super().speak(sound)
class Dachshund(Dog):
    def speak(self, sound='Piux'):
        return f"{self.name} says {sound}"
class Bulldog(Dog):
    def speak(self, sound='Boofx'):
        return f"{self.name} says {sound}"
class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)


#miles = Dog('Miles',4,' Jack Russell Terrier')
#buddy = Dog('Buddy',9,' Dachshund')
#jack = Dog('Jack',3,' Bulldog')
#jim = Dog('Jim',5,' Bulldog')


miles = JackRussellTerrier('Miles',4)
buddy = Dachshund('Buddy',9)
jack = Bulldog('Jack',3)
jim = Bulldog('Jim',5)
jimx = Bulldog("Jimx",5)
hal = GoldenRetriever('Hal',6)

print(miles.species)
print(miles.speak('Frrrr'))
print(buddy.name)
print(jack)
print(jim.speak())
print(jim.speak('Grrrr'))
print(type(miles))
print(isinstance(miles,Bulldog))
print(jim.speak('Grrrx'))
print(hal.speak())

"""
    Define a class, which is a sort of blueprint for an object
    Instantiate an object from a class
    Use attributes and methods to define the properties and behaviors of an object
    Use inheritance to create child classes from a parent class
    Reference a method on a parent class using super()
    Check if an object inherits from another class using isinstance()
"""
