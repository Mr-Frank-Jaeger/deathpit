#!/bin/python3
# weapon.py

#define weapons
class Weapon:
    weapons = []
    def __init__(self, name, damage, armor_damage, cost, description='a weapon'):
        self.name = name
        self.damage = damage
        self.armor_damage = armor_damage
        self.cost = cost
        self.description = description 
        #add weapon instance to weapons ledger/array
        #Weapon.weapons is needed so we know weapons[] is from the Weapon class
        Weapon.weapons.append(self)



#Sword is a subclass of Weapon (inheratance)
class Sword(Weapon):
    #every fuction method always gets self
    def __init__(self):
        #super calls the constructor of the parent class Weapon
        super().__init__('Sword', 25, 10, 100)
        self.description = 'Damocles would be proud'
        print(self.name)


class Mace(Weapon):
    def __init__(self):
        super().__init__('Mace', 15, 20, 115)
        self.description = 'Bashes the fuck out of armor at the cost of damage'


class Dagger(Weapon):
    def __init__(self):
        super().__init__('Dagger', 10, 5, 25)
        self.description = 'pokey pokey stab stab'

