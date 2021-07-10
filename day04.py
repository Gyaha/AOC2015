import hashlib


def find_zero_hash(s: str, c: int) -> int:
    r = ""
    n = 0
    t = "0" * c
    while r[:c] != t:
        n += 1
        r = hashlib.md5((s + str(n)).encode()).hexdigest()
    return n


with open("input04") as file:
    data = file.read()
    print(find_zero_hash(data, 5))
    print(find_zero_hash(data, 6))
