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

    options = set()

    for a, b in replacements.items():

        last = -1
        location = molecule.find(a, last+1)
        while location != -1:
            for bb in b:
                trans = molecule[:location] + bb + molecule[location+len(a):]
                options.add(trans)
            last = location
            location = molecule.find(a, last + 1)

    solution = len(options)

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
