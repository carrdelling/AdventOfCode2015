

def solve(data):

    t_row, t_col = [int(x.split()[-1]) for x in data[:-1].split(',')[1:]]

    value = 20151125
    row, col = 1, 1

    while (row != t_row) or (col != t_col):
        value = (value * 252533) % 33554393

        if row > 1:
            col += 1
            row -= 1
        else:
            row = col + 1
            col = 1

    solution = value

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
