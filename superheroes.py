import random

DEBUG = True # var for enabling console logs for debugging

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self):
        if DEBUG:
            print(random.randint((self.max_damage/2), self.max_damage))
        return random.randint((self.max_damage/2), self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, start_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = start_health
        self.current_health = start_health
        self.deaths = 0
        self.kills = 0

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
        turn = 0 # controls who is attacking each iteration
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
    
    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        self.deaths += num_deaths

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    
    def remove_hero(self, name):
        for hero in range(len(self.heroes)):
            if self.heroes[hero].name == name:
                self.heroes.pop(hero)
                return
        return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        attacker = self.heroes[random.randint(0, len(self.heroes - 1))]
        defender = other_team.heroes[random.randint(0, len(other_team.heroes - 1))]
        attacker.fight(defender)
    
    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            kdr = hero.kills / hero.deaths
            print(f'{hero.name}: {kdr} KDR')