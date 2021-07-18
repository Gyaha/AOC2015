def letter_to_int(c: chr) -> int:
    return ord(c) - 97


def int_to_letter(i: int) -> chr:
    return chr(i + 97)


def convert_to_p(s: str) -> list:
    return [letter_to_int(a) for a in s]


def convert_to_s(p: list) -> str:
    return "".join([int_to_letter(a) for a in p])


BANNED_LETTERS = [letter_to_int(a) for a in "iol"]
HIGEST_LETTER = letter_to_int("z")


def check_password(p: list) -> bool:
    return check_banned(p) and check_straight(p) and check_pairs(p)


def check_banned(p: list) -> bool:
    for bl in BANNED_LETTERS:
        if bl in p:
            return False
    return True


def check_straight(p: list) -> bool:
    for i in range(len(p) - 2):
        n = p[i]
        if n == p[i + 1] - 1 == p[i + 2] - 2:
            return True
    return False


def check_pairs(p: list) -> bool:
    i = 0
    n = 0
    while i < len(p) - 1:
        if p[i] == p[i + 1]:
            n += 1
            i += 1
        i += 1
        if n >= 2:
            return True
    return False


def next_password(p: list) -> list:
    def add_n(p, i) -> bool:
        p[i] += 1
        if p[i] > HIGEST_LETTER:
            p[i] = 0
            return True
        return False
    i = len(p) - 1
    while add_n(p, i):
        i -= 1
    return p


def next_valid_password(s: str) -> str:
    p = convert_to_p(s)
    next_password(p)
    while not check_password(p):
        next_password(p)
    return convert_to_s(p)


with open("input11") as file:
    data = file.read()
    print(next_valid_password(data))
    print(next_valid_password("hepxxyzz"))
