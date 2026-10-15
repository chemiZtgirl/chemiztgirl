class Human:
    __name = "JM"; __age = 34; __birthday = "October 22, 1992"

    @property
    def name(self):
        return f"I am {self.__name}. "

    @property 
    def age(self):
        return f"I am {self.__age} years old. "

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age

H = Human()
H.name = "Sir Bern"
H.age = -30
print(H.name + H.age)
