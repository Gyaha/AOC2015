def find_lowest_that_gets(s: str):
    t = int(s) // 10
    l = t // 2
    h = [0 for _ in range(l)]
    for e in range(1, l):
        if h[e] + e >= t:
            return e
        for i in range(e, l, e):
            h[i] += e


def find_new_lowest_that_gets(s: str):
    t = int(s)
    h = [0 for _ in range(t // 2)]
    for e in range(len(h)):
        if h[e] + (e * 11) >= t:
            return e
        for i in range(1, 51):
            j = i * e
            if j >= len(h):
                break
            h[j] += (e * 11)


with open("input20") as file:
    data = file.read()
    print(find_lowest_that_gets(data))
    print(find_new_lowest_that_gets(data))
