from card import Card


class Attack(object):

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __str__(self):
        return f'source: {self.source} --> target: {self.target}'

    def __hash__(self):
        return hash((self.source, self.target))

    def target_after_attack(self):
        raise NotImplementedError

    def target_dies(self):
        return self.target.hp <= self.source.attack

    def source_after_attack(self):
        raise NotImplementedError()

    def source_dies(self):
        raise NotImplementedError()


class WarriorAttack(Attack):

    def __init__(self, source, target):
        super().__init__(source, target)

    def __eq__(self, other):
        return isinstance(other, Card) and self.source == other.source and self.target == other.target

    def __hash__(self):
        return hash((self.source, self.target))

    def target_after_attack(self):
        if self.target_dies():
            return None
        return Card(self.target.name, self.target.mana, self.target.attack, self.target.hp - self.source.attack)

    def source_after_attack(self):
        if self.source_dies():
            return None
        return Card(self.source.name, self.source.mana, self.source.attack, self.source.hp - self.target.attack)

    def source_dies(self):
        return self.source.hp <= self.target.attack


class PlayerAttack(Attack):

    def __init__(self, source, target):
        super().__init__(source, target)

    def __hash__(self):
        return hash((self.source, self.target))

    def __eq__(self, other):
        return isinstance(other, PlayerAttack) and self.source == other.source and self.target == other.target
