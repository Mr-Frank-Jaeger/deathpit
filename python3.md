#!/bin/python3
#python3 notes

#output var type
type(my_var).__name__

#f-strings have dynamic values
#use instead of +
num_bullets = 10
my_var = f"you have {num_bullets} bullets"
print(my_var)

#print() returns a value of None
#f-statments return values

# set var to no value or empty value
my_var = None

# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)

#functions
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

gem_stone = area_of_circle(5)

#functions that have 2 inputs and 2 returns
def become_warrior(full_name, power):
    title = f'{full_name} the warrior'
    new_power = power + 1
    return title, new_power

become_warrior(tim, 10)

#can set default values for variables
#if no armor is set the default is 0

def get_punched(health, armor=0):
    damage = 50 - armor
    new_health = health - damage
    return new_health

#return 2 values from a function
def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25
    return lesser_cursed, greater_cursed

#import custom classes
#Weapon.py has the class weapon with an inheratance sub class of Mace
#in main.py add:
# import custom classes
from weapon import Mace
from charater import Charater
 
