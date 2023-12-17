

def solve(data):

    program = [tuple(x.replace(',', '') for x in row.split()) for row in data]

    ip = 0
    registers = {'a': 0, 'b': 0}

    while -1 < ip < len(program):

        ins = program[ip]

        if ins[0] == 'inc':
            registers[ins[1]] += 1
        if ins[0] == 'hlf':
            registers[ins[1]] = int(registers[ins[1]] // 2)
        if ins[0] == 'tpl':
            registers[ins[1]] = registers[ins[1]] * 3
        if ins[0] == 'jmp':
            delta = int(ins[1].replace('+', '').strip())
            ip += delta
            continue

        if ins[0] == 'jie':
            if registers[ins[1]] % 2 == 0:
                delta = int(ins[2].replace('+', '').strip())
                ip += delta
                continue

        if ins[0] == 'jio':
            if registers[ins[1]] == 1:
                delta = int(ins[2].replace('+', '').strip())
                ip += delta
                continue
        ip += 1

    solution = registers['b']

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
