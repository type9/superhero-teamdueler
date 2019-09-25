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
        if attack_amount < 0: # stops from adding health if block amount is larger than attack amount
            attack_amount = 0
        new_health = self.current_health - attack_amount
        self.current_health = new_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        return True
    
    def fight(self, opponent):
        turn = 1 # controls who is attacking each iteration
        while self.is_alive() and opponent.is_alive():
            turn += 1 # because it starts at 2, self will always attack first
            if (turn % 2) == 0:
                attack_damage = self.attack()
                print(f'{self.name} attacks {opponent.name} for {attack_damage} damage.')
                opponent.take_damage(attack_damage)
            else:
                attack_damage = opponent.attack()
                print(f'{opponent.name} attacks {self.name} for {attack_damage} damage.')
                self.take_damage(attack_damage)
            print(f'{self.name} is at {self.current_health} health. {opponent.name} is at {opponent.current_health} health.\n')
        if opponent.is_alive():
            print(f'Opponent {opponent.name} is victorious')
        else:
            print(f'Hero {self.name} is victorious')