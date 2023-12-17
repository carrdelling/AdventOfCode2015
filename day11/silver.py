import string
ALPHABET = string.ascii_lowercase


def next_pass(password):

    rev = list(password)[::-1]

    for i, c in enumerate(rev):
        if c == 'z':
            rev[i] = 'a'
        elif c == 'h':
            rev[i] = 'j'
            break
        elif c == 'k':
            rev[i] = 'm'
            break
        elif c == 'n':
            rev[i] = 'p'
            break
        else:
            rev[i] = chr(ord(c) + 1)
            break

    return ''.join(rev[::-1])


def has_pairs(password):

    idx = 0
    count = 0

    while idx <= len(password) - 2:
        if password[idx] == password[idx + 1]:
            count += 1
            idx += 2

            if count > 1:
                return True
        else:
            idx += 1
    return False


def has_straight(password):
    for i in range(len(password) - 2):
        if password[i:i + 3] in ALPHABET:
            return True
    return False


def is_valid(password):

    if any(x in password for x in 'ilo'):
        return False
    if not has_pairs(password):
        return False

    return has_straight(password)


def solve(data):

    current = data

    current = next_pass(current)

    while not is_valid(current):
        current = next_pass(current)

    solution = current

    return solution


def main():
    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
