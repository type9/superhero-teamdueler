import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, start_health):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = start_health
        self.current_health = start_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        attack_damage = 0
        for ability in range(len(self.abilities)):
            attack_damage =+ self.abilities[ability].attack()
        return attack_damage

    def add_armor(self, armor):
        self.armors.append(armor)
    def defend(self):
        block_amount = 0
        for armor in range(len(self.armors)):
            block_amount =+ self.armors[armor].block()
        return block_amount
    
    def take_damage(self, damage):
        attack_amount = damage - self.defend()
        if attack_amount < 0:
            attack_amount = 0
        new_health = self.current_health - attack_amount
        self.current_health = new_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        return True
    
    def fight(self, opponent):
        pass