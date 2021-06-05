class Driver:
    def __init__(self, name, age, car, position):
        self.name = name
        self.age = age
        self.car = car
        self.position = position
  
    def overtake(self):
        self.position -= 1
        print("Hello my name is " + self.name + " I just smoked u bro. New position = " + str(self.position))
    
    def pit (self):
        print(self.name + " is pitting to change his tyres.")


class F1driver(Driver):
    def __init__(self, name, age, car, position, hoecount):
        self.name = name
        self.age = age
        self.car = car
        self.position = position
        self.hoecount = hoecount
    
    def getHoes():
        self.hoecount += 1
    
    def monaccoHoes():
        print("Monnaco hoe time")
        


class Gt3driver(Driver):
    def __init__(self, name, age, car, position, hoecount):
        self.name = name
        self.age = age
        self.car = car
        self.position = position
        self.hoecount = -10
        
    def brokewithnohoes():
        print(":((((((((")
        
# ------------------------------------------------------------

Botas = F1driver("botas", 21, "Merc", 2, 10)

Botas.getHoes()

FrankWanky = Gt3driver("frankywanky", 44, "slow", 9, -10)


print(FrankWanky.name)

Botas.overtake()
Botas.pit()