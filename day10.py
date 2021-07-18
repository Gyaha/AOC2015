def look_and_say(input: list, rounds: int):
    for _ in range(rounds):
        input = look_and_say_round(input)
    return len(input)


def look_and_say_round(input: list):
    def add_output(output: list, i: int, j: int):
        output.append(i)
        output.append(j)
    output = []
    l, n = input[0], 0
    for i in input:
        if not l == i:
            add_output(output, n, l)
            n = 0
        l = i
        n += 1
    add_output(output, n, l)
    return output


def str_to_list(s: str) -> list:
    return [int(l) for l in s]


with open("input10") as file:
    data = file.read()
    print(look_and_say(str_to_list(data), 40))
    print(look_and_say(str_to_list(data), 50))
