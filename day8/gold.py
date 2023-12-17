
def solve(data):

    solution = 0

    for rule in data:

        full = rule.strip()
        to_encode = rule.count('"') + rule.count('\\')

        extra = to_encode + 2
        solution += extra

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
