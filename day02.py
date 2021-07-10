def paper_per_box(s: str) -> int:
    h, w, l = [int(a) for a in s.split("x")]
    a = [h * w, h * l, w * l]
    a.sort()
    return a[0] + (sum(a) * 2)


def total_paper_for_boxes(s: str) -> int:
    total = 0
    for l in s.splitlines():
        total += paper_per_box(l)
    return total


def ribbon_per_box(s: str) -> int:
    d = [int(a) for a in s.split("x")]
    d.sort()
    return (d[0] * 2) + (d[1] * 2) + (d[0] * d[1] * d[2])


def total_ribbon(s: str) -> int():
    t = 0
    for l in s.splitlines():
        t += ribbon_per_box(l)
    return t


print(ribbon_per_box("2x3x4"))

with open("input02") as file:
    data = file.read()
    print(total_paper_for_boxes(data))
    print(total_ribbon(data))
