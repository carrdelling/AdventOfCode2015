import hashlib


def solve(data):

    solution = None
    current = 0
    while solution is None:
        target = f"{data}{current}".encode()
        h = hashlib.md5(target).hexdigest()

        if h[:5] == '00000':
            solution = current
        else:
            current += 1

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
