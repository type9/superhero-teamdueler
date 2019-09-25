import superheroes

debug_ability = superheroes.Ability("Debugging Ability", 20)
assert (0 <= debug_ability.attack() <= 20), "Ability.attack() generated out of range"

debug_ability_1 = superheroes.Ability("Debugging Ability", 30)

debug_block = superheroes.Armor("Debug block", 20)
assert (0 <= debug_block.block() <= 20), "Armor.block() generated out of range"

test_hero = superheroes.Hero("Grace Hopper", 200)
print(test_hero.name)
print(test_hero.current_health)
test_hero.add_ability(debug_ability)
test_hero.add_ability(debug_ability_1)
test_hero.add_armor(debug_block)
print(test_hero.abilities)
print(test_hero.attack())
test_hero.take_damage(50)
print(test_hero.current_health)
print("Tests run without errors")