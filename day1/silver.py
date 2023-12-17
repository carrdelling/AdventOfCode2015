from collections import Counter


def solve(data):

    solution = Counter(data)['('] - Counter(data)[')']
    
    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
