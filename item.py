#!/bin/python3
# item.py

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Key(Item):
    def __init__(self):
        super().__init__('Key', 'An old rusty key, I wonder what it goes too?')

class Chest(Item):
    def __init__(self, locked=True, contents=None):
        super().__init__('Chest', 'A wooden chest with a rusty old lock.')
        self.locked = locked
        self.contents = contents if contents else []

    def unlock(self, key):
        # unlock chest with key
        if isinstance(key, Key):
            self.locked = False
            print('You unlocked the chest with the key!\n')
            return True
        else:
            print('That won\'t unlock this chest.\n')

    def open(self):
        # open chest and see contents
        if self.locked:
            print('The chest is locked. You need a key.')
        else:
            print('You open the chest and find:')
            for item in self.contents:
                if hasattr(item, 'name'):
                    print(f' - {item.name}')
                else:
                    print(f' - {item}')
            print()
            items = self.contents
            self.contents = []
            return items

class Dickbutt(Item):
    def __init__(self):
        super().__init__('Tiny Figurine', 'A tiny figurine of what looks like a dick coming out of a butt that has a funny face.')

class Armor(Item):
    def __init__(self, armor_rating):
        super().__init__('Armor', 'Armor that can be equiped')
        self.armor_rating = 10
        
