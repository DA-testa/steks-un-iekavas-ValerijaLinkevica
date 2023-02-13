# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return 1
            else:
                if are_matching(opening_brackets_stack.pop(), next):
                    if i+1 == len(text):
                        return "Success"
                    else:
                        pass
                else:
                    return i + 1
            pass


def main():
    choice = input()

    if "F" in choice:
        filename = input()
        usefile = filename + '.txt'
        file = open(usefile, 'r')
        line = file.readline()
        mismatch = find_mismatch(line)

        if not mismatch:
            print("Success")
        else:
            print(mismatch)
    elif "I" in choice:
        text = input()
        mismatch = find_mismatch(text)

        if not mismatch:
            print("Success")
        else:
            print(mismatch)
    else:
        print("Error in input choice")


if __name__ == "__main__":
    main()
