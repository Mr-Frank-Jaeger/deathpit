#!/bin/python3
# armor.py

#define armor
class Armor:
    armors = []
    def __init__(self, name, armor_rating, cost, description='a peice of armor'):
        self.name = name
        self.armor_rating = armor_rating
        self.cost = cost
        self.description = description 
        #add armor instance to armors ledger/array
        #Armor.armors is needed so we know armors[] is from the Armor class
        Armor.armors.append(self)



#Leather_Armor is a subclass of Armor (inheratance)
class Leather_Armor(Armor):
    #every fuction method always gets self
    def __init__(self):
        #super calls the constructor of the parent class Armors
        super().__init__('Leather Armor', 10, 75)
        self.description = 'A simple leather vest'
        print(self.name)
