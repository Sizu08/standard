from enum import Enum


class Clan(Enum):
    ROYALPALADIN = "Royal Paladin"


class Gift(Enum):
    FORCE = "Force"
    PROTECT = "Protect"
    ACCEL = "Accel"
    NONE = "None"


class Trigger(Enum):
    CRITICAL = "Critical"
    DRAW = "Draw"
    HEAL = "Heal"
    NONE = "None"


class Nation(Enum):
    UNITEDSANCTUARY = "United Sanctuary"


class Race(Enum):
    HUMAN = "Human"
    COSMODRAGON = "Cosmo Dragon"
    HIGHBEAST = "High Beast"
    GIANT = "Giant"
    SYLPH = "Sylph"
    ELF = "Elf"


class Position(Enum):
    LEFTFRONT = 1
    CENTERFRONT = 2
    RIGHTFRONT = 3
    LEFTBACK = 4
    CENTERBACK = 5
    RIGHTBACK = 6
    DAMAGE = 7


class Game:
    def __init__(self, id, players, field):
        self.id = id
        self.players = players
        self.field = field
        self.turn = 1

    def getPlayer(self, id):
        return self.players[id]


class Player:
    def __init__(self, id, name, deck, hand):
        self.id = id
        self.name = name
        self.deck = deck
        self.hand = hand
        self.damage = Zone(id, Position.DAMAGE, [])

    def getName(self):
        return self.name


class Deck:
    def __init__(self, player, name, cards):
        self.player = player
        self.name = name
        self.cards = cards


class Zone:
    def __init__(self, player, position, cards):
        self.position = position
        self.player = player
        self.cards = cards


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)
