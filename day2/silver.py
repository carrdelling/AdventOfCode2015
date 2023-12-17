

def solve(data):

    solution = sum(2*a*b + 2*b*c +2*c*a + min(a*b, b*c, c*a) for a, b, c in data)

    return solution


def main():
    with open('input') as in_f:
        data = [tuple(map(int, row.strip().split('x'))) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
