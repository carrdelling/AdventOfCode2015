

def make_cookie(n):

    recipe = [0, 0, 0, 0]

    for i in range(n+1):
        recipe[0] = i
        rest = n - i
        for j in range(rest+1):
            recipe[1] = j
            rest2 = rest - j
            for k in range(rest2 + 1):
                recipe[2] = k
                rest3 = rest2 - k

                # last must make up to 100
                recipe[3] = rest3

                yield recipe


def solve(data):

    SIZE = 100
    CALORIES = 500
    ingredients = {}
    i_names = []
    for row in data:
        name, spec = row.strip().split(': ')
        spec = [int(x.split()[-1]) for x in spec.split(', ')]
        ingredients[name] = tuple(spec)
        i_names.append(name)

    best = 0
    for option in make_cookie(SIZE):

        # mix it
        mix = [0, 0, 0, 0, 0]
        for idx, ing in enumerate(i_names):
            for j, v in enumerate(ingredients[ing]):
                mix[j] += v * option[idx]

        # score it
        if any(v <= 0 for v in mix):
            score = 0
        elif mix[-1] != 500:
            score = 0
        else:
            score = mix[0] * mix[1] * mix[2] * mix[3]

        best = max(best, score)

    solution = best

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
