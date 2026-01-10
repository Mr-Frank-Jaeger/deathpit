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
from item import Key, Chest, Dickbutt
from armor import Leather_Armor

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
            dex = 20
        elif p_class_pick == '2':
            p_class = 'Rogue'
            health = 75
            armor = 15
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
    entrance = Room('Cave Entrance', 'A dark cave stands before you screaming from the mountain')
    hallway = Room('Stone Hallway', 'A stone corridor with torches on the walls.')
    arena = Room('Death Pit Areaa', 'The infamous death pit! Bones litter the floor')
    treasure = Room('Tresure Room', 'A small room holding but only a single chest')

    # connect rooms (bidirectional)
    #entrance
    entrance.add_exit('north', hallway)
    hallway.add_exit('south', entrance)
    gerblin = Character('Gerblin', 50, 5, Dagger(), 5)
    entrance.add_enemy(gerblin)
    gerblin.drops.append(Leather_Armor())

    # hallway
    hallway.add_exit('north', arena)
    arena.add_exit('south', hallway)
    hallway.add_exit('east', treasure)
    treasure.add_exit('west', hallway)

    #treasure
    chest = Chest(locked=True, contents=[Dickbutt()])
    treasure.add_item(Chest())

    #arena
    arena.add_enemy(Character('Gerblin', 50, 5, Dagger(), 5))
    orc = Character('Orc', 75, 10, Mace(), 0)
    orc.drops.append(Key())
    arena.add_enemy(orc)

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
            sword     25        10
            mace      20        25
            dagger    15        5
    You have two acations: attack and defend:
        attack: swing with you weapon. damage = weapon damage - defender's armor
        defend: increase armor by 5 to a max of 25. I hope you enjoy!

    Once you find and unlock the chest you have won!

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
            choice = input(Fore.GREEN + 'What do you want to do? (move/take/use/equip/inventory/equipment/quit): ').lower() 
            try:
                # User is impatient and sends something like 'move north' or 'take 1'
                action, tgt = choice.split()
            except ValueError:
                action = choice
            else:
                try:
                    item_num = int(tgt)
                except ValueError:
                    # target of action is not a number; must be a direction
                    item_num = None
                    direction = tgt.strip()
                else:
                    direction = None

            if action == 'quit':
                print('Thanks for playing!')
                playing = False

            elif action == 'inventory':
                player.show_inventory()

            elif action == 'equipment':
                player.show_equipment()

            #take or equip items
            elif action == 'take':
                if current_room.items:
                    print('Items in room:')
                    for i, item in enumerate(current_room.items):
                        print(f'{i+1}. {item.name}')

                    if not item_num:
                        item_num = input('Which item? (enter number): ')
                    try:
                        item_index = int(item_num) - 1
                        if 0 <= item_index < len(current_room.items):
                            item = current_room.items[item_index]

                            #cant pick up chests
                            if isinstance(item, Chest):
                                print('The chest is too heavy to carry!\n')
                            else:
                                player.add_item(item)
                                current_room.remove_item(item)
                    except:
                        print('Invalid choice!\n')
                else:
                    print('Nothing here to take.\n')
            
            elif action == 'equip':
                print('Items in your inventory:')
                for i, item in enumerate(player.inventory):
                    print(f'{i+1}. {item.name}')

                item_num = input('What do you want to equip? (enter number): ')
                try:
                    item_index = int(item_num) - 1
                    if 0 <= item_index < len(player.inventory):
                        item = player.inventory[item_index]
                        player.equip_item(item)
                except:
                    print('Invalid choice!\n')

            elif action == 'use':
                if current_room.items:
                    #check for chests
                    chest = None
                    for item in current_room.items:
                        if isinstance(item, Chest):
                            chest = item
                            break
    
                    if chest:
                        if chest.locked:
                            key = player.has_item(Key)
                            if key:
                                chest.unlock(key)
                                chest_contents = chest.open()
                                if chest_contents:
                                    for item in chest_contents:
                                        current_room.add_item(item)
                            else:
                                print('Chest is locked and you need a key.\n')
                        else:
                            chest.open()
                    else:
                        print('nothing to use here.\n')

            elif action == 'move':
                if current_room.exits:
                    if not direction:
                        direction = get_direction_from_user(current_room.exits)
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


def get_direction_from_user(exits: dict) -> str:
    """Prompt the user to move in a direction.

    If only one direction is possible, an empty input chooses that by default.

    Args:
        exits: Options for movement from the given room

    Returns: Direction to move in.
    """
    exit_options = list(exits.keys())
    exit_options_str = ", ".join(exit_options)
    choice_prompt = f"Which direction? ({exit_options_str}): "
    choice = input(choice_prompt).lower()

    only_choice = exit_options[0] if len(exit_options) == 1 else None
    if only_choice and not choice:
        print(f"Empty selection, defaulting to {only_choice}")
        return only_choice
    else:
        return choice
    


# call main to start game
if __name__ == '__main__':
    while True:
        main()

