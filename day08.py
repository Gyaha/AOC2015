def list_value(s: str) -> int:
    v = 0
    for l in s.splitlines():
        v += line_value(l)
    return v


def line_value(s: str) -> int:
    t = len(s)
    n = 0
    i = 1
    while i < t - 1:
        if s[i] == "\\":
            if not s[i + 1] == "x":
                i += 2
            else:
                i += 4
        else:
            i += 1
        n += 1
    return t - n


def list_encode(s: str) -> int:
    v = 0
    for l in s.splitlines():
        v += line_encode(l)
    return v


def line_encode(s: str) -> int:
    t = len(s)
    n = 6
    i = 1
    while i < t - 1:
        if s[i] == "\\" or s[i] == "\"":
            n += 1
        i += 1
        n += 1
    return n - t


with open("input08") as file:
    data = file.read()
    print(list_value(data))
    print(list_encode(data))
