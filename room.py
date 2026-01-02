#!/bin/python3
# room.py

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.enemies = []
        self.items = []

    def add_exit(self, direction, room):
        # add exit to another room
        self.exits[direction] = room

    def add_enemy(self, enemy):
        # add enemy to this room
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def describe(self):
        #describe room to player
        print(f'\n== {self.name} ==')
        print(self.description)

        if self.enemies:
            print(f'Enemies here: {", ".join([e.name for e in self.enemies])}')

        if self.items:
            print(f'Items here: {", ".join([i.name for i in self.items])}')

        if self.exits:
            print(f'Exits: {", ".join(self.exits.keys())}')
        print()
