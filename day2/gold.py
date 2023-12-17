

def solve(data):

    solution = sum(a*b*c + min(a+a+b+b, c+c+b+b, a+a+c+c) for a, b, c in data)

    return solution


def main():
    with open('input') as in_f:
        data = [tuple(map(int, row.strip().split('x'))) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
