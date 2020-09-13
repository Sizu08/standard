class Card:
    def __init__(self, name, grade, gift, trigger, power, critical,
                 nation, clan,  race, effect, sentinel):
        self.name = name
        self.grade = grade
        self.gift = gift
        self.power = power
        self.critical = critical
        self.nation = nation
        self.clan = clan
        self.race = race
        self.effect = effect
        self.sentinel = sentinel

    def cardName(self):
        return self.name
