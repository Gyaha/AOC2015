def read_instructions(data: str):
    inst = []
    for l in data.splitlines():
        ll = l.split()
        if ll[0] == "jmp":
            inst.append((ll[0], read_number(ll[1])))
        elif ll[0] == "jio" or ll[0] == "jie":
            inst.append((ll[0], ll[1][0], read_number(ll[2])))
        else:
            inst.append((ll[0], ll[1]))
    return inst


def read_number(s: str) -> int:
    n = int(s[1:])
    if s[0] == "-":
        n = -n
    return n


def run_instructions(inst: list, a: int, b: int):
    pointer = 0
    while pointer < len(inst):
        i = inst[pointer]
        if i[0] == "hlf":
            v = get_val(a, b, i[1])
            v //= 2
            a, b = set_val(a, b, i[1], v)
            pointer += 1
        elif i[0] == "tpl":
            v = get_val(a, b, i[1])
            v *= 3
            a, b = set_val(a, b, i[1], v)
            pointer += 1
        elif i[0] == "inc":
            v = get_val(a, b, i[1])
            v += 1
            a, b = set_val(a, b, i[1], v)
            pointer += 1
        elif i[0] == "jmp":
            pointer += i[1]
        elif i[0] == "jie":
            v = get_val(a, b, i[1])
            if v % 2 == 0:
                pointer += i[2]
            else:
                pointer += 1
        else:  # "jio":
            v = get_val(a, b, i[1])
            if v == 1:
                pointer += i[2]
            else:
                pointer += 1
    return a, b


def get_val(a, b, r):
    if r == "a":
        return a
    else:
        return b


def set_val(a, b, r, v):
    if r == "a":
        a = v
    else:
        b = v
    return a, b


def get_b_after(data: str, a: int, b: int):
    inst = read_instructions(data)
    a, b = run_instructions(inst, a, b)
    return b


with open("input23") as file:
    data = file.read()
    print(get_b_after(data, 0, 0))
    print(get_b_after(data, 1, 0))
