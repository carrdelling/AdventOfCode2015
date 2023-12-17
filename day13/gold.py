from itertools import permutations


def solve(data):

    happiness = {}
    people = set()
    best = -1E10

    for row in data:
        chunks = row.replace('.', '').split()
        s, e = chunks[0], chunks[-1]
        v = int(chunks[3]) * (-1 if 'lose' in row else 1)

        happiness[(s, e)] = v
        people.add(s)

    for p in people:
        happiness[(p, 'Yourself')] = 0
        happiness[('Yourself', p)] = 0
    people.add('Yourself')

    for option in permutations(people):
        option_score = sum(happiness[(a, b)] + happiness[(b, a)] for a, b in zip(option, option[1:]))
        option_score += happiness[(option[-1], option[0])] + happiness[(option[0], option[-1])]

        best = max(best, option_score)

    solution = best

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
