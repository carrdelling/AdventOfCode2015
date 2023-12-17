
def solve(data):

    ITERATIONS = 40

    current = data
    for _ in range(ITERATIONS):

        prev = None
        count = 0
        next_word = ''
        for i in current:

            if i == prev:
                count += 1
            else:
                if prev is not None:
                    next_word += f"{count}{prev}"
                prev = i
                count = 1
        else:
            next_word += f"{count}{prev}"

        current = next_word

    solution = len(current)

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
