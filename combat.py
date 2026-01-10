#!/bin/python3
# combat.py
# turn based text rpg game test

#imports
import random
import time
from colorama import Fore, Style, init

# create combat function
def combat(player, room):
    #combat, returns True if player wins
    enemies = room.enemies

    print(Fore.RED + '======')
    print(Fore.RED + 'FIGHT!')
    print(Fore.RED + '======')

    #create combat loop
    combat = True
    while combat:
        #player turn
        print(Fore.RED + f'===ENEMIES===')
        for i, enemy in enumerate(enemies):
            print(Fore.RED + f'{i+1}. {enemy.name} - Health: {enemy.health} Armor: {enemy.armor}')

        player.stats()
        choice = input(Fore.GREEN + 'Your turn (attack or defend): ').lower()

        try:
            # User is impatient and sends something like 'attack [NUM]'
            action, target_num = choice.split()
        except ValueError:
            action = choice
            target_num = None

        if action == 'attack':
            if not target_num:
                target_num = input('Which enemy? (enter number): ')
            print()
            try:
                target_index = int(target_num) - 1
                if 0 <= target_index < len(enemies):
                    target = enemies[target_index]
                    player.attack(target)

                    if not target.is_alive():
                        print(f'The {target.name} is defeated!\n')
                        
                        # drop item?
                        if target.drops:
                            for item in target.drops:
                                room.add_item(item)
                                print(f'{target.name} dropped {item.name}!\n')
                        room.remove_enemy(target)

                        if len(enemies) == 0:
                            print('All enemies are defeated!\n')
                            return True
                else:
                    print('Invalid target! It must be an enemy listed.\n')
                    continue
            except:
                print('Invalid target! Pick a number.\n')
                continue

        elif action == 'defend':
            if target_num:
                print("You cannot defend against a specific target; entering defensive stance.")
            player.defend()
        else:
            print("NOPE! either attack or defend\n")
            continue

        #enemy turn
        for enemy in enemies:
            print(Fore.RED + f"----------------------")
            print(Fore.RED + f"{enemy.name}'s turn...")
            print(Fore.RED + f"----------------------")
            time.sleep(2)

            #if only 1 enemey it will never do nothing
            if len(enemies) == 1:
                enemy_action = random.randint(1,2)
            else:
                enemy_action = random.randint(1,3)

            if enemy_action == 1:
                enemy.attack(player)
                if not player.is_alive():
                    print(Fore.RED + f'YOU DIED\n')
                    return False
            elif enemy_action == 2:
                enemy.defend()
            elif enemy_action == 3:
                enemy.do_nothing()

    return True

