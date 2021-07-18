def read_rules(s: str) -> list:
    rules = []
    for l in s.splitlines():
        ll = l.split()
        rules.append((int(ll[3]), int(ll[6]), int(ll[13])))
    return rules


def travel_deers(s: str, time: int) -> int:
    rules = read_rules(s)
    d = []
    for r in rules:
        d.append(travel_for(r, time))
    d.sort(reverse=True)
    return d[0]


def points_deer(s: str, time: int) -> int:
    rules = read_rules(s)
    points = [0 for _ in range(len(rules))]
    for t in range(time):
        dist = [0 for _ in range(len(rules))]
        for i in range(len(rules)):
            dist[i] = travel_for(rules[i], t + 1)
        t = max(dist)
        for j in range(len(dist)):
            if dist[j] == t:
                points[j] += 1
    points.sort(reverse=True)
    return points[0]


def travel_for(deer: tuple, time: int) -> int:
    t = (time // (deer[1] + deer[2])) * (deer[0] * deer[1])
    r = min((time % (deer[1] + deer[2])), deer[1]) * deer[0]
    return t + r


with open("input14") as file:
    data = file.read()
    print(travel_deers(data, 2503))
    print(points_deer(data, 2503))
