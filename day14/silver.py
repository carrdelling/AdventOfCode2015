

def solve(data):

    reinders = []
    LIMIT = 2503

    for row in data:
        chunks = row.replace('.', '').split()
        name, speed = chunks[0], chunks[3]
        t, rest = chunks[6], chunks[13]

        reinders.append((name, int(speed), int(t), int(rest)))

    best = 0

    for n, speed, energy, r in reinders:

        full_cycle = energy + r
        n_full = LIMIT // full_cycle
        rest = LIMIT % full_cycle
        distance = n_full * energy * speed
        distance += min(energy, rest) * speed

        best = max(best, distance)

    solution = best

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
