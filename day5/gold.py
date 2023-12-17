
def solve(data):

    nice = 0

    for word in data:
        is_nice = False
        for a, b in zip(word, word[2:]):
            if a == b:
                is_nice = True
                break

        if not is_nice:
            continue

        for i in range(len(word)-1):
            pattern = word[i:i+2]
            if pattern in word[i+2:]:
                nice += 1
                break

    solution = nice

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
