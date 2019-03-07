from card import Card


class Attack(object):

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __str__(self):
        return f'source: {self.source} --> target: {self.target}'


class WarriorAttack(Attack):

    def __init__(self, source, target):
        super().__init__(source, target)

    def target_after_attack(self):
        if self.target_dies():
            return None
        return Card(self.target.name, self.target.mana, self.target.attack, self.target.hp - self.source.attack)

    def target_dies(self):
        return self.target.hp <= self.source.attack


class PlayerAttack(Attack):

    def __init__(self, source, target):
        super().__init__(source, target)
