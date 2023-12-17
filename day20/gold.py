

def solve(data):

    target = data[0]
    solution = None
    SIZE = 1000000
    ELF_RATIO = 11
    MAX_DELIVERIES = 50

    houses = [0] * (SIZE+1)

    for i in range(1, SIZE+1):
        idx = i
        deliveries = MAX_DELIVERIES
        while deliveries > 0:
            if idx > SIZE:
                break
            houses[idx] += i
            deliveries -= 1

            idx += i

    for i in range(1, SIZE+1):
        if (houses[i] * ELF_RATIO) >= target:
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
