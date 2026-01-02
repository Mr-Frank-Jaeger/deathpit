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
#TODO: add rooms, exits, descriptions of rooms and things



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

    #create list of enemies in the room
    enemies = []
    enemies.append(Character('Gerblin', 50, 5, Sword(), 10))
    enemies.append(Character('Orc', 75, 10, Mace(), 0))


    print(Fore.CYAN + '======')
    print(Fore.CYAN + 'FIGHT!')
    print(Fore.CYAN + '======\n')


    #create combat loop
    combat = True
    action = ""
    while combat == True:
        #player turn
        print(Fore.RED + f'===ENEMIES===')
        for i, enemy in enumerate(enemies):
            print(Fore.RED + f'{i+1}. {enemy.name} - Health: {enemy.health} Armor: {enemy.armor}')
        player.stats()
        action = input(Fore.GREEN + 'Your turn (attack or defend): ')
        if action == "attack":
            target_num = input('Which enemy? (enter number): ')
            target_index = int(target_num) - 1
            if 0 <= target_index < len(enemies):
                target = enemies[target_index]
                player.attack(target)
            else:
                print('You are lose your concentration...')
                continue
            #check for if its dead
            if not target.is_alive():
                print(f'The {target.name} is dead!\n')
                enemies.remove(target)
                if len(enemies) == 0:
                    print('All enemies are defeated!\n')
                    print('You survived the Death Pit!!!\n')
                    combat = False
                    break
        elif action == "defend":
            player.defend()
        else:
            print("NOPE! either attack or defend\n")
            continue

        #enemy turn
        for enemy in enemies:
            #enemy.stats()      
            print(Fore.RED + f"----------------------")
            print(Fore.RED + f"{enemy.name}'s turn...")
            print(Fore.RED + f"----------------------")
            time.sleep(2)
            enemy_action = random.randint(1,3)
            if enemy_action == 1:
                enemy.attack(player)
                if not player.is_alive():
                    print(Fore.RED + f'YOU DIED\n')
                    combat = False
                    break
            elif enemy_action == 2:
                enemy.defend()
            elif enemy_action == 3:
                enemy.do_nothing()
    pass

# call main to start game
if __name__ == '__main__':
    while True:
        main()

