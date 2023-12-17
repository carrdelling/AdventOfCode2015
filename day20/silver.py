

def solve(data):

    target = data[0] // 10  # because every elf hands 10 presents
    solution = None
    SIZE = 1000000

    houses = [0] * (SIZE+1)

    for i in range(1, SIZE+1):
        idx = i
        while True:
            if idx > SIZE:
                break
            houses[idx] += i

            idx += i

    for i in range(1, SIZE+1):
        if houses[i] >= target:
            solution = i
            break

    return solution


def main():
    with open('input') as in_f:
        data = [int(r.strip()) for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
