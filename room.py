#!/bin/python3
# room.py

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.enemies = []

    def add_exit(self, direction, room):
        # add exit to another room
        self.exits[direction] = room

    def add_enemy(self, enemy):
        # add enemy to this room
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def describe(self):
        #describe room to player
        print(f'\n== {self.name} ==')
        print(self.description)

        if self.enemies:
            print(f'Enemies here: {", ".join([e.name for e in self.enemies])}')

        if self.exits:
            print(f'Exits: {", ".join(self.exits.keys())}')
        print()
