class Animal:
    name = ""
    sound = ""
    def makeSound(self):
        print(self.sound)

class Cow(Animal):
    name = "Cow"
    sound = "Moo"

class Cat(Animal):
    name = "Cat"
    sound = "Meow"

cow = Cow()
cat = Cat()
cow.makeSound()
cat.makeSound()
