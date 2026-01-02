#!/bin/python3
# character.py

#imports
import random

#define player class
class Character:
    def __init__(self, name, health, armor, weapon, dex):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon
        self.dex = dex

    def attack(self, target):
        dodge_chance = random.randint(1,100)
        dodge_chance += target.dex
        if dodge_chance >=90:
            print(f'{self.name} swings at {target.name}...')
            print(f'{target.name} dodged the attack!\n')
            return
        damage = int(self.weapon.damage - target.armor)
        if damage <= 0:
            damage = 1
        target.health -= damage
        target.armor -= int(self.weapon.armor_damage)
        if target.armor <= 0:
            target.armor = 0
        print(f'{self.name} hits {target.name} for {damage} damage.\n')

    def defend(self):
        self.armor += int(self.armor + 5)
        if self.armor >= 25:
            self.armor = 25
        print(f'{self.name} changes to defensive stance and increased armor to {self.armor}\n')

    def do_nothing(self):
        print(f'{self.name} does nothing...\n')

    def is_alive(self):
        return self.health > 0

    def stats(self):
        print('---------------------------------')
        print(f'{self.name} health:{self.health} armor:{self.armor} weapon:{self.weapon.name}')
        print('---------------------------------')

