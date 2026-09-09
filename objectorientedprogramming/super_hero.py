class SuperHero:
    name : str
    power : str
    universe: str

    def __init__(self,name,power,universe):
        self.name = name
        self.power = power
        self.universe = universe
    def get_superhero(self):
        print(self.name,self.power,self.universe)

superhero_instance1 = SuperHero("spiderman","web","marvel")
superhero_instance2 = SuperHero("batman","rich","dc")
superhero_instance3 = SuperHero("superman","fly","dc")

superhero_instance1.get_superhero()
superhero_instance2.get_superhero()
superhero_instance3.get_superhero()