

SCAN = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
""".split('\n')


def solve(data):

    sue = {}
    for row in data:
        chunks = row.strip().split(': ')
        name = chunks[0]
        spec = ': '.join(chunks[1:])
        number = int(name.replace('Sue ', ''))
        spec = {x.split(': ')[0]: int(x.split(': ')[1]) for x in spec.split(', ')}

        sue[number] = spec

    parsed_scan = {x.split(': ')[0]: int(x.split(': ')[1]) for x in SCAN if ':' in x}

    solution = -1

    for name in sue:

        for req in parsed_scan:
            if req in sue[name]:
                if parsed_scan[req] != sue[name][req]:
                    break
        else:
            solution = name
            break

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
