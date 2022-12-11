def check_num(a: str):
    a = a.strip()
    if not a.isnumeric():
        return False

    return True


def operation(l, x):
    if "+" in l:
        s = l.split("+")
        o = "+"

    else:
        s = l.split("-")
        o = "-"

    s[0] = s[0].strip()
    s[1] = s[1].strip()
    space = " " * (max(len(s[0]), len(s[1])) + 2)
    # rjust is used to add spaces to the left of the string with the total length of the string with the spaces
    print(s[0].rjust(len(space)))
    print(o + s[1].rjust(len(space) - 1))
    print("-" * len(space))
    if o == "-":
        result = int(s[0]) - int(s[1])

    else:
        result = int(s[0]) + int(s[1])

    if x:
        print(str(result).rjust(len(space)))


def check(l: list[str]):
    for i in range(len(l)):
        if "+" in l[i]:
            n = l[i].split("+")
            if not check_num(n[0]) or not check_num(n[1]):
                return "Error: Numbers must only contain digits."

            elif len(n[0]) > 5 or len(n[1]) > 5:
                return "Error: Numbers cannot be more than four digits."

        elif "-" in l[i]:
            n = l[i].split("-")
            if not check_num(n[0]) or not check_num(n[1]):
                return "Error: Numbers must only contain digits."

            elif len(n[0]) > 5 or len(n[1]) > 5:
                return "Error: Numbers cannot be more than four digits."

        else:
            return "Error: Operator must be '+' or '-'."

    return False


def arithmetic_arranger(l: list[str], x=False):
    if len(l) > 5:
        return "Error: Too many problems."

    # Check for the errors
    if check(l):
        return check(l)

    for i in range(len(l)):
        operation(l[i], x)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
