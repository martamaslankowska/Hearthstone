class Card(object):

    def __init__(self, name, mana, attack, health):
        self.name = name
        self.mana = mana
        self.attack = attack
        self.hp = health



    def __str__(self):
        return f'{self.name} ({self.mana}) - {self.attack} att | {self.hp} hp'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        return isinstance(o, Card) and o.name == self.name and o.mana == self.mana \
               and o.attack == self.attack and o.hp == self.hp

    def __hash__(self):
        return hash((self.name, self.mana, self.attack, self.hp))

CARDS = [Card('Arcanite Reaper', 5, 5, 2), Card('Bloodfen Raptor', 2, 3, 2), Card('Boulderfist Ogre', 6, 6, 7),
         Card('Chillwind Yeti', 4, 4, 5), Card('Core Hound', 7, 9, 5), Card('Fiery War Axe', 3, 3, 2),
         Card("Light's Justice", 1, 1, 4), Card('Magma Rager', 3, 5, 1), Card('Murloc Raider', 1, 2, 1),
         Card('Oasis Snapjaw', 4, 2, 7)]
