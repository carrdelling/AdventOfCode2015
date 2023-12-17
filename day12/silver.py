import json


def get_score(element):

    score = 0

    if isinstance(element, dict):
        for v in element.values():
            score += get_score(v)

    elif isinstance(element, list):
        for v in element:
            score += get_score(v)
    elif isinstance(element, int):
        score += element
    else:
        pass

    return score


def solve(data):

    encoded = json.loads('\n'.join(data))

    score = get_score(encoded)

    solution = score

    return solution


def main():
    with open('input') as in_f:
        data = [r for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
