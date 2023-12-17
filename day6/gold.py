from itertools import product

def solve(data):

    size = 1000

    rules = []
    for row in data:

        chunks = row.strip().split()

        if 'turn' in chunks[0]:

            r_type = 1 if chunks[1] == 'on' else -1
            x_min, y_min = map(int, chunks[2].split(','))
            x_max, y_max = map(int, chunks[4].split(','))

        else:

            r_type = 2
            x_min, y_min = map(int, chunks[1].split(','))
            x_max, y_max = map(int, chunks[3].split(','))

        rule = (r_type, x_min, x_max, y_min, y_max)
        rules.append(rule)

    brightness = 0
    for idx, (px, py) in enumerate(product(range(size), repeat=2)):

        if idx % 100_000 == 0:
            print(idx, brightness)

        light = 0

        for r_type, x_min, x_max, y_min, y_max in rules:

            if (x_min <= px <= x_max) and (y_min <= py <= y_max):
                light = max(0, light + r_type)

        brightness += light

    solution = brightness

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
