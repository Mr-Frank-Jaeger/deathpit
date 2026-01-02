#!/bin/python3
# main.py
# turn based text rpg game test

#imports
import random
import time
from colorama import Fore, Style, init

#import custom classes
from character import Character
from weapon import Sword, Mace, Dagger
from room import Room
from combat import combat

#charater creator
def create_character():
    while True:
        print('=== Charater Creation ===\n')

        name = input('Enter your charater\'s name: ')

        print('Classes...')
        print('1: Warrior - HP:100, Armor:20, Dex: 10%, and a Sword.')
        print('2: Rogue - HP:75, Armor:20, Dex: 40%, and a Dagger.')
        p_class_pick = input('Enter your class (number): ')
        if p_class_pick == '1':
            p_class = 'Warrior'
            health = 100
            armor = 20
            weapon = Sword() 
            dex = 10
        elif p_class_pick == '2':
            p_class = 'Rogue'
            health = 75
            armor = 10
            weapon = Dagger() 
            dex = 40
        else:
            print('Invalid choice, try again...\n')
            continue

        player = Character(name, health, armor, weapon, dex)
        print(f'You are a {p_class} named {name} and you are wield a {weapon.name}.\n')
        return player

#define Rooms
def create_world():
    # create rooms and connect

    #create rooms
    entrance = Room('Cave Entrance', 'A dark cave stands before you before the mountain')
    hallway = Room('Stone Hallway', 'A stone corridor with torches on the walls.')
    arena = Room('Death Pit Areaa', 'The infamous death pit! Bones litter the floor')
    treasure = Room('Tresure Room', 'A small room holding but only a single chest')

    # connect rooms (bidirectional)
    #entrance
    entrance.add_exit('north', hallway)
    hallway.add_exit('south', entrance)
    entrance.add_enemy(Character('Gerblin', 50, 5, Dagger(), 15))

    # hallway
    hallway.add_exit('north', arena)
    arena.add_exit('south', hallway)
    hallway.add_exit('east', treasure)
    treasure.add_exit('west', hallway)

    #treasure

    #arena
    arena.add_enemy(Character('Gerblin', 50, 5, Dagger(), 15))
    arena.add_enemy(Character('Orc', 75, 10, Mace(), 0))

    # return the starting room
    return entrance



# def main function
def main():

    #initialize colorama
    init(autoreset=True)

    print(Fore.CYAN + '=====================')
    print(Fore.CYAN + 'Welcome to Death Pit!')
    print(Fore.CYAN + '=====================\n')

    #alpha description
    print('''
    This is intended to be a text adventure MUD. You will create a charater
    and then be dropped into the death pit to fight a few enemies. 
    You and enenimes have:
        HP: if you don't know what this is find another game nerd.
        Armor: a value that midigates damage
        Dex: a dodge% + the base games dodge% of 10%
        weapon: sword, dagger, or mace. Weapons always damage armor even if
        only 1 damage is dealt. 
            weapon  damage  armor_damage
            sword   25  10
            mace    20  25
            dagger  15  5
    You have two acations: attack and defend:
        attack: swing with you weapon. damage = weapon damage - defender's armor
        defend: increase armor by 5 to a max of 25. I hope you enjoy!

    ''')

    #start character creation
    player = create_character()

    # create world
    current_room = create_world()



    # main game loop
    playing = True
    while playing and player.is_alive():
        # show current room
        current_room.describe()

        # if enemies in room, must fight
        if current_room.enemies:
            combat_result = combat(player, current_room)
            if not combat_result:
                playing = False
                break
        else:
            # no enemies, player can move or quit
            action = input(Fore.GREEN + 'What do you want to do? (move/quit): ').lower() 

            if action == 'quit':
                print('Thanks for playing!')
                playing = False
            elif action == 'move':
                if current_room.exits:
                    direction = input(f'Which direction? ({", ".join(current_room.exits.keys())}): ').lower()
                    if direction in current_room.exits:
                        current_room = current_room.exits[direction]
                        print(f'\nYou move {direction}...\n')
                        time.sleep(1)
                    else:
                        print('You cannot go that way!\n')
                else:
                    print('There are no exits! You are trapped!\n')
            else:
                print('Invalid command!\n')

# call main to start game
if __name__ == '__main__':
    while True:
        main()

