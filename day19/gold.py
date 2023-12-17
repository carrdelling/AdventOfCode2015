from collections import defaultdict


def solve(data):

    replacements = defaultdict(list)
    molecule = ''
    for row in data:

        if '=>' in row:
            a, b = row.split(' => ')
            replacements[a].append(b)
        elif len(row) > 5:
            molecule = row

    # just going backwards seems to work (!)
    count = 0
    while molecule != 'e':
        for src, repl in replacements.items():
            for r in repl:
                if r in molecule:
                    molecule = molecule.replace(r, src, 1)
                    count += 1

    solution = count

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
