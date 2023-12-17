from itertools import combinations


def select_group(target_w, elements, size):

    for subset in combinations(elements, size):
        if sum(subset) == target_w:
            yield subset


def valid_partition_single(items, target):

    # the partition is valid if there is at least another single group split
    for solution_size in range(1, len(items) - 2):
        for _ in select_group(target, items, solution_size):
            return True

    return False


def valid_partition(items, target, size_main):

    # the partition is valid if there is at least another single group split
    for solution_size in range(1, size_main+1):
        for candidate in select_group(target, items, solution_size):
            rest = [x for x in items if x not in candidate]
            if valid_partition_single(rest, target):
                return True

    return False


def solve(data):

    target = sum(data) // 4
    best_qe = 1E99
    all_items = {x for x in data}

    for solution_size in range(1, len(data)-3):

        for candidate in select_group(target, data, solution_size):
            rest = [x for x in all_items if x not in candidate]
            if valid_partition(rest, target, solution_size):
                qe = candidate[0]
                for c in candidate[1:]:
                    qe *= c
                best_qe = min(best_qe, qe)

        else:
            if best_qe < 1E98:
                break

    solution = best_qe

    return solution


def main():
    with open('input') as in_f:
        data = [int(r.strip()) for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
