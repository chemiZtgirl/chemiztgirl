class Human:
    __name = "JM"; __age = 34; __birthday = "October 22, 1992"
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return f"I am {self.__name}. "
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def get_age(self):
        return f"I am {self.__age} years old. "

H = Human()
H.set_name("Sir Bern")
H.set_age(-30)
print(H.get_name())
print(H.get_age())
