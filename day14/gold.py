from collections import defaultdict

def solve(data):

    reinders = {}
    LIMIT = 2503

    for row in data:
        chunks = row.replace('.', '').split()
        name, speed = chunks[0], chunks[3]
        t, rest = chunks[6], chunks[13]

        reinders[name] = int(speed), int(t), int(rest)

    # SIM!


    points = {}
    distance = {}
    energy = {}
    resting = {}

    for n in reinders:
        points[n] = 0
        distance[n] = 0
        energy[n] = reinders[n][1]
        resting[n] = 0

    for _ in range(LIMIT):

        for n in reinders:

            # resting
            if resting[n] > 0:
                if resting[n] == 1:
                    resting[n] = 0
                    energy[n] = reinders[n][1]
                else:
                    resting[n] -= 1
            else:
                # moving
                if energy[n] == 0:
                    pass
                else:
                    distance[n] += reinders[n][0]
                    if energy[n] == 1:
                        energy[n] = 0
                        resting[n] = reinders[n][2]
                    else:
                        energy[n] -= 1
        # scoring
        max_d = max(distance.values())
        for n in reinders:

            if distance[n] == max_d:
                points[n] += 1

    solution = max(points.values())

    return solution


def main():
    with open('input') as in_f:
        data = [r.strip() for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":
    main()
