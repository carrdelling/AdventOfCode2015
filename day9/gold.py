
def solve(data):

    distances = {}
    cities = set()

    for rule in data:
        chunks = rule.split()
        a, b, c = chunks[0], chunks[2], int(chunks[-1])
        distances[(a, b)] = c
        distances[(b, a)] = c
        cities.add(a)
        cities.add(b)

    paths = [(tuple([c]), 0) for c in cities]
    max_cost = 0

    while len(paths) > 0:
        current, cost = paths.pop()

        if len(current) == len(cities):
            max_cost = max(max_cost, cost)
            continue

        for city in cities:
            if city in current:
                continue
            n_path = tuple(list(current) + [city])
            n_cost = cost + distances[(current[-1], city)]

            paths.append((n_path, n_cost))

    solution = max_cost

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
