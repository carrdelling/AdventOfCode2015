

def solve(data):

    current = 0, 0
    seen = {current}

    for c in data:

        move = {'v': (-1, 0),
                '>': (0, 1),
                '^': (1, 0),
                '<': (0, -1),
                }[c]

        current = current[0] + move[0], current[1] + move[1]
        seen.add(current)

    solution = len(seen)

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
