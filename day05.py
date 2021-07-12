nice_letters = ['a', "e", "i", "o", "u"]
bad_words = ["ab", "cd", "pq", "xy"]


def check_words(s: str) -> int:
    lines = s.splitlines()
    t = 0
    for l in lines:
        if check_word(l):
            t += 1
    return t


def check_word(s: str) -> bool:
    return check_bad(s) and check_count(s) and check_twice(s)


def check_bad(s: str) -> bool:
    for b in bad_words:
        if b in s:
            return False
    return True


def check_twice(s: str) -> bool:
    p = ""
    for l in s:
        if l == p:
            return True
        p = l
    return False


def check_count(s: str) -> bool:
    t = 0
    for nl in nice_letters:
        t += s.count(nl)
        if t >= 3:
            return True
    return False


def new_check_words(s: str) -> int:
    lines = s.splitlines()
    t = 0
    for l in lines:
        if new_check_word(l):
            t += 1
    return t


def new_check_word(s: str) -> bool:
    return check_pair(s) and check_repeats(s)


def check_pair(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i:i + 2] in s[:i] + "**" + s[i + 2:]:
            return True
    return False


def check_repeats(s: str) -> bool:
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


with open("input05") as file:
    data = file.read()
    print(check_words(data))
    print(new_check_words(data))
