from itertools import product

STEPS = 100
STAY_ON = {2, 3}
SWITCH_ON = {3}


def neighbours(p):

    i, j = p

    for ii, jj in product([-1, 0, 1], repeat=2):
        if ii == 0 and jj == 0:
            continue
        yield i + ii, j + jj


def solve(data):

    panel = set()
    for i, row in enumerate(data):
        for j, l in enumerate(row):
            if l == '#':
                panel.add((i, j))

    panel |= {(0, 0), (0, 99), (99, 0), (99, 99)}

    for _ in range(STEPS):

        new_panel = set()

        for i in range(len(data)):
            for j in range(len(data[0])):
                power = sum(1 for neigh in neighbours((i, j)) if neigh in panel)

                if (i, j) in panel and power in STAY_ON:
                    new_panel.add((i, j))
                if (i, j) not in panel and power in SWITCH_ON:
                    new_panel.add((i, j))

        panel = {x for x in new_panel}
        panel |= {(0, 0), (0, 99), (99, 0), (99, 99)}

    solution = len(panel)

    return solution


def main():
    with open('input') as in_f:
        data = [list(r.strip()) for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
