class animal:
    def __init__ (self,type,habitat):
        self.type = type
        self.habitat = habitat

class elephant(animal):
    def __init__ (self,type,habitat):
        animal.__init__ (self,type,habitat)

print("Single inheritance :")            
Jumbo = elephant("Herbivorous","Savannah")
print("Type of Jumbo :",Jumbo.type)
print("Habitat of Jumbo :",Jumbo.habitat)

class circus_elephant(elephant):
    def __init__(self, type, habitat):
        super().__init__(type, habitat)

    def balanceball(self):
        print("I am bouncing a ball !")
    def playcricket(self):
        print("I play cricket !")
    def cycle(self):
        print("I am riding a cycle !")

print("\nMulti level inheritance :")    
Appu = circus_elephant("Herbivorous", "Kerala")
Appu.cycle()
Appu.balanceball()
Appu.playcricket()