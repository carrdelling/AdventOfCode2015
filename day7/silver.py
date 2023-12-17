MAX_VALUE = 65535


def parse_int(x):

    try:
        return int(x)
    except:
        return None


def apply_rule(rule, memory):

    ops, target = rule

    if len(ops) == 1:
        # <var> -> <var>
        if ops[0] in memory:
            return target, memory[ops[0]]
        else:
            return None

    if ops[0] == 'NOT':
        # NOT <var> -> <var>
        if ops[1] in memory:
            v = MAX_VALUE - memory[ops[1]]
            return target, v
        else:
            return None

    if ops[1] == 'LSHIFT':
        if ops[0] in memory:
            v = memory[ops[0]] << int(ops[2])
            return target, v
        else:
            return None

    if ops[1] == 'RSHIFT':
        if ops[0] in memory:
            v = memory[ops[0]] >> int(ops[2])
            return target, v
        else:
            return None

    if ops[1] == 'AND':
        a = parse_int(ops[0])
        if a is None and ops[0] in memory:
            a = memory[ops[0]]
        b = parse_int(ops[2])
        if b is None and ops[2] in memory:
            b = memory[ops[2]]

        if (a is None) or (b is None):
            return None
        else:
            v = a & b
            return target, v

    if ops[1] == 'OR':
        a = parse_int(ops[0])
        if a is None and ops[0] in memory:
            a = memory[ops[0]]
        b = parse_int(ops[2])
        if b is None and ops[2] in memory:
            b = memory[ops[2]]

        if (a is None) or (b is None):
            return None
        else:
            v = a | b
            return target, v


def solve(data):

    rules = []
    memory = {}
    for row in data:
        ops_raw, target = row.split(' -> ')
        ops = ops_raw.split()
        rule = (ops, target)
        rules.append(rule)

    # init with some assignations
    used = set()
    for idx in range(len(rules)):
        r = rules[idx]
        ins, target = r
        if len(ins) < 2:
            v = parse_int(ins[0])
            if v is not None:
                memory[target] = v
                used.add(idx)

    for x in sorted(used)[::-1]:
        rules = rules[:x] + rules[x+1:]

    while 'a' not in memory:
        new_rules = []

        for rule in rules:

            result = apply_rule(rule, memory)

            if result is None:
                new_rules.append(rule)
            else:
                memory[result[0]] = result[1]

        rules = list(new_rules)

    solution = memory['a']

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
