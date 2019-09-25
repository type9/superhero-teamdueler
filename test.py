import superheroes

debug_ability = superheroes.Ability("Debugging Ability", 20)
assert (0 <= debug_ability.attack() <= 20), "Ability.attack() generated out of range"

debug_ability_1 = superheroes.Ability("Debugging Ability 1", 30)

debug_block = superheroes.Armor("Debug block", 20)
assert (0 <= debug_block.block() <= 20), "Armor.block() generated out of range"

debug_block_1 = superheroes.Armor("Debug block 1", 30)

test_hero = superheroes.Hero("Grace Hopper", 200)
test_hero_1 = superheroes.Hero("John Stickler", 150)

test_hero.add_ability(debug_ability)
test_hero.add_armor(debug_block)
test_hero_1.add_ability(debug_ability_1)
test_hero_1.add_armor(debug_block_1)

test_hero.fight(test_hero_1)