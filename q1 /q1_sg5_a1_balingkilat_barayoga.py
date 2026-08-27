class hero:
    def __init__(self,name,hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self,damage):
        self.hp -= damage
        print(self.name,"has taken", damage, "damage! He/She is at", self.hp, "health!")


myHero = hero("Arthur",120)
myHero2 = hero("Morgana", 115)

myHero.take_damage(10)

