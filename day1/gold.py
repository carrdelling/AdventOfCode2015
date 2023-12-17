

def solve(data):

    floor = 0
    solution = None
    for idx, c in enumerate(data):
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1

        if floor == -1:
            solution = idx + 1
            break

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
