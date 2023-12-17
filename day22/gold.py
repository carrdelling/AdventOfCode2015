import heapq

def solve(data):

    boss_hp = int(data[0].split()[-1])
    boss_damage = int(data[1].split()[-1])

    POISON_DAMAGE = 3
    DRAIN_DAMAGE = 2
    MANA_RECHARGE = 101
    MISSILE_DAMAGE = 4
    CURSE_DAMAGE = 1
    SHIELD_ARMOR = 7

    hp = 50
    mana = 500
    mana_spent = 0
    shield = 0
    poison = 0
    recharge = 0

    min_cost = 1E9

    states = [(mana_spent, hp, mana, boss_hp, shield, poison, recharge, tuple())]

    while states:
        current = list(heapq.heappop(states))

        # 1) apply states
        current[1] -= CURSE_DAMAGE
        if current[1] <= 0:
            continue

        if current[4] > 0:
            # shield
            current[4] -= 1

        if current[5] > 0:
            current[5] -= 1
            current[3] -= POISON_DAMAGE

            if current[3] <= 0:
                min_cost = min(current[0], min_cost)
                print(min_cost, current[-1])
                continue

        if current[6] > 0:
            current[6] -= 1
            current[2] += MANA_RECHARGE

        # 2) choose a spell
        for spell in ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']:

            _mana_spent = current[0]
            _hp = current[1]
            _mana = current[2]
            _boss_hp = current[3]
            _shield = current[4]
            _poison = current[5]
            _recharge = current[6]

            _actions = list(current[-1])
            _actions.append((spell, _mana))

            # 3) apply spell
            if spell == 'Magic Missile':
                cost = 53
                _mana_spent += cost
                _mana -= cost

                if _mana < 0:
                    continue
                if _mana_spent >= min_cost:
                    continue

                _boss_hp -= MISSILE_DAMAGE
                if _boss_hp <= 0:
                    min_cost = min(_mana_spent, min_cost)
                    print(min_cost, _actions)
                    continue

            if spell == 'Drain':
                cost = 73
                _mana_spent += cost
                _mana -= cost

                if _mana < 0:
                    continue
                if _mana_spent >= min_cost:
                    continue

                _boss_hp -= DRAIN_DAMAGE
                _hp += DRAIN_DAMAGE

                if _boss_hp <= 0:
                    min_cost = min(_mana_spent, min_cost)
                    print(min_cost, _actions)
                    continue

            if spell == 'Shield':
                if _shield > 0:
                    continue

                cost = 113
                _mana_spent += cost
                _mana -= cost

                if _mana < 0:
                    continue
                if _mana_spent >= min_cost:
                    continue

                _shield = 6

            if spell == 'Poison':
                if _poison > 0:
                    continue

                cost = 173
                _mana_spent += cost
                _mana -= cost

                if _mana < 0:
                    continue
                if _mana_spent >= min_cost:
                    continue

                _poison = 6

            if spell == 'Recharge':
                if _recharge > 0:
                    continue

                cost = 229
                _mana_spent += cost
                _mana -= cost

                if _mana < 0:
                    continue
                if _mana_spent >= min_cost:
                    continue

                _recharge = 5

            # 4) Pre-boss turn
            got_shield = False
            if _shield > 0:
                # shield
                got_shield = True
                _shield -= 1

            if _poison > 0:
                _poison -= 1
                _boss_hp -= POISON_DAMAGE

                if _boss_hp <= 0:
                    min_cost = min(_mana_spent, min_cost)
                    print(min_cost, _actions)
                    continue

            if _recharge > 0:
                _recharge -= 1
                _mana += MANA_RECHARGE

            # 5) Boss turn
            damage = boss_damage - SHIELD_ARMOR if got_shield > 0 else boss_damage
            _hp -= damage

            if _hp <= 0:
                continue

            # 6) Next round
            new_state = (_mana_spent, _hp, _mana, _boss_hp, _shield, _poison, _recharge, tuple(_actions))
            heapq.heappush(states, new_state)

    solution = min_cost

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
