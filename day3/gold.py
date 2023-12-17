

def solve(data):

    santa = 0, 0
    robo = 0, 0
    seen = {santa, robo}

    last = 'robo'
    for c in data:

        move = {'v': (-1, 0),
                '>': (0, 1),
                '^': (1, 0),
                '<': (0, -1),
                }[c]

        if last == 'robo':
            santa = santa[0] + move[0], santa[1] + move[1]

            seen.add(santa)
            last = 'santa'
            continue

        if last == 'santa':
            robo = robo[0] + move[0], robo[1] + move[1]

            seen.add(robo)
            last = 'robo'
            continue

    solution = len(seen)

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
