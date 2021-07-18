def eval_all_numbers(s: str):
    a = eval(s)
    n = []
    extract_all_numbers(a, n)
    return sum(n)


def extract_all_numbers(a, n: list):
    for b in a:
        if type(b) is int:
            # print(b)
            n.append(b)
        elif type(b) is list:
            extract_all_numbers(b, n)
        elif type(b) is dict:
            extract_all_numbers(list(b.values()), n)


def eval_most_numbers(s: str):
    a = eval(s)
    n = []
    extract_most_numbers(a, n)
    return sum(n)


def extract_most_numbers(a, n: list):
    for b in a:
        if type(b) is int:
            n.append(b)
        elif type(b) is list:
            extract_most_numbers(b, n)
        elif type(b) is dict:
            if "red" in b.keys() or "red" in b.values():
                continue
            extract_most_numbers(b.values(), n)


with open("input12") as file:
    data = file.read()
    print(eval_all_numbers(data))
    print(eval_most_numbers(data))
