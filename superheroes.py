import random

DEBUG = False # var for enabling console logs for debugging

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

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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
            self.add_death(1)
            opponent.add_kill(1)
        else:
            print(f'Hero {self.name} is victorious')
            self.add_kill(1)
            opponent.add_death(1)
    
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

    def is_alive(self):
        for hero in self.heroes:
            if hero.is_alive() == True:
                return True
        return False

    def attack(self, other_team):
        turn = 0 # controls who is attacking
        while self.is_alive() and other_team.is_alive():
            turn += 1
            attacker = self.heroes[random.randint(0, len(self.heroes) - 1)]
            defender = other_team.heroes[random.randint(0, len(other_team.heroes) - 1)]
            if (turn / 2) == 0:
                attacker.fight(defender)
            else:
                defender.fight(attacker)
        if self.is_alive:
            return 1 # returns number of winning team
        else:
            return 2

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            kdr = hero.kills / hero.deaths
            print(f'{hero.name}: {kdr} KDR')

    def get_avg_kdr(self):
        total_kills = 0
        total_deaths = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        if total_deaths == 0: # checks for division by 0
            return total_kills # returns just kills instead
        else:
            return total_kills/total_deaths
    def print_team_status(self):
        for hero in self.heroes:
            if hero.is_alive():
                print(f'[ALIVE] {hero.name}')
            else:
                print(f'[DEAD] {hero.name}')

class Arena:
    def __init__(self):
        team_one = None
        team_two = None
        last_winner = 0 # should be 1 or 2
        
    def create_ability(self):
        name = input('Input a name for the ability: ')
        max_damage = input('Input the max damage the ability can deal: ')
        new_ability = Ability(name, int(max_damage))
        return new_ability
    
    def create_weapon(self):
        name = input('Input a name for the weapon: ')
        max_damage = input('Input the max damage that weapon can deal: ')
        new_weapon = Weapon(name, int(max_damage))
        return new_weapon

    def create_armor(self):
        name = input('Input a name for the armor: ')
        max_block = input('Input the max damage that armor can mitigate: ')
        new_armor = Armor(name, int(max_block))
        return new_armor

    def create_hero(self):
        name = input('Input a hero name: ')
        max_health = input('Input the max_health for that hero: ')
        new_hero = Hero(name, int(max_health))
        still_adding = True
        while still_adding:
            print('If you would like to add an ability input 1, for weapon input 2, and for armor input 3.')
            user_input = input('Type anything else to skip: ')
            if user_input == '1':
                new_hero.add_ability(self.create_ability())
            elif user_input == '2':
                new_hero.add_weapon(self.create_weapon())
            elif user_input == '3':
                new_hero.add_armor(self.create_armor())
            else:
                still_adding = False
        return new_hero
    
    def build_team_one(self):
        name = input('Input a name for Team 1: ')
        new_team = Team(name)
        still_adding = True
        while still_adding:
            print('If you would like to add a character input 1')
            user_input = input('Otherwise type anything else: ')
            if user_input == '1':
                new_team.add_hero(self.create_hero())
            else:
                still_adding = False
        self.team_one = new_team
    
    def build_team_two(self):
        name = input('Input a name for Team 2: ')
        new_team = Team(name)
        still_adding = True
        while still_adding:
            print('If you would like to add a character input 1')
            user_input = input('Otherwise type anything else: ')
            if user_input == '1':
                new_team.add_hero(self.create_hero())
            else:
                still_adding = False
        self.team_two = new_team
    
    def team_battle(self):
        self.last_winner = self.team_one.attack(self.team_two)

    def show_stats(self):
        if self.last_winner == 1: # checks the winner of the last run team battle
            print(f'{self.team_one.name} won!')
        else:
            print(f'{self.team_one.name} won!')
        print(f'========= {self.team_one.name} Stats =========')
        print(f'Average KDR: {self.team_one.get_avg_kdr()}')
        self.team_one.print_team_status()
        print(f'========= {self.team_two.name} Stats =========')
        print(f'Average KDR: {self.team_two.get_avg_kdr()}')
        self.team_two.print_team_status()

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()