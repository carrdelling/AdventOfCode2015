

def solve(data):

    nice = 0

    blacklist = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in data:
        is_nice = False
        for a, b in zip(word, word[1:]):
            if a == b:
                is_nice = True
                break
        if not is_nice:
            continue
            
        n_vowels = 0
        for v in vowels:
            n_vowels += word.count(v)
        if n_vowels < 3:
            continue

        for b in blacklist:
            if b in word:
                break
        else:
            nice += 1

    solution = nice

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
