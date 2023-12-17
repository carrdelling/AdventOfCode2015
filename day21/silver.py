

WEAPONS_SHOP = {
    'Dagger': (8, 4),
    'Shortsword': (10, 5),
    'Warhammer': (25, 6),
    'Longsword': (40, 7),
    'Greataxe': (74, 8),
}

ARMOR_SHOP = {
    'Leather': (13, 1),
    'Chainmail': (31, 2),
    'Splintmail': (53, 3),
    'Bandedmail': (75, 4),
    'Platemail': (102, 5),
}

RINGS_SHOP = {
    'Damage +1': (25, 1, 0),
    'Damage +2': (50, 2, 0),
    'Damage +3': (100, 3, 0),
    'Defense +1': (20, 0, 1),
    'Defense +2': (40, 0, 2),
    'Defense +3': (80, 0, 3),
}


def buy_sets():

    full_sets = []
    for weapon in list(WEAPONS_SHOP):
        aw = WEAPONS_SHOP[weapon][1]
        cw = WEAPONS_SHOP[weapon][0]
        for armor in list(ARMOR_SHOP) + ['None']:
            da = ARMOR_SHOP.get(armor, (0, 0))[1]
            ca = ARMOR_SHOP.get(armor, (0, 0))[0] + cw
            for ring1 in list(RINGS_SHOP) + ['None1']:
                ar1 = RINGS_SHOP.get(ring1, (0, 0, 0))[1] + aw
                dr1 = RINGS_SHOP.get(ring1, (0, 0, 0))[2] + da
                cr1 = RINGS_SHOP.get(ring1, (0, 0, 0))[0] + ca
                for ring2 in list(RINGS_SHOP) + ['None2']:
                    if ring2 == ring1:
                        continue
                    ar2 = RINGS_SHOP.get(ring2, (0, 0, 0))[1] + ar1
                    dr2 = RINGS_SHOP.get(ring2, (0, 0, 0))[2] + dr1
                    cr2 = RINGS_SHOP.get(ring2, (0, 0, 0))[0] + cr1

                    full_sets.append((cr2, ar2, dr2))

    return full_sets


def battle(hp, damage, armor, boss_hp, boss_damage, boss_armor):

    player = hp
    boss = boss_hp

    p_damage = max(1, damage - boss_armor)
    b_damage = max(1, boss_damage - armor)

    result = None

    while result is None:
        # player
        boss -= p_damage

        if boss <= 0:
            result = True
            continue

        # boss
        player -= b_damage
        if player <= 0:
            result = False
            continue

    return result


def solve(data):

    boss_hp = int(data[0].split()[-1])
    boss_damage = int(data[1].split()[-1])
    boss_armor = int(data[2].split()[-1])

    player_hp = 100

    solution = -1
    equip_sets = sorted(buy_sets())

    for c, d, a in equip_sets:
        combat_result = battle(player_hp, d, a, boss_hp, boss_damage, boss_armor)

        if combat_result:
            solution = c
            break

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
