
def solve(data):

    solution = 0

    for rule in data:

        full = rule.strip()
        clean = full[1:-1]
        clean = clean.replace(r'\\', 'B').replace(r'\"', 'A')
        ascii = clean.count(r'\x')

        extra = len(full) - (len(clean) - (ascii*3))
        solution += extra

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
