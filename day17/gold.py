from itertools import combinations

EGGNOG = 150


def solve(data):

    counts = 0

    for l in range(1, len(data)):
        for c in combinations(data, r=l):
            if sum(c) == EGGNOG:
                counts += 1
        if counts > 0:
            break

    solution = counts

    return solution


def main():
    with open('input') as in_f:
        data = [int(r.strip()) for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
