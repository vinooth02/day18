class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says:Bow Bow!")

class Cat(Animal):

    def sound(self):

        print("Cat says:Meow meow!")

def startprogarm():

    dog=Dog()
    cat=Cat()

    dog.sound()
    cat.sound()

startprogarm()
