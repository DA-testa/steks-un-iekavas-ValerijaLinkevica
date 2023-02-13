# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return 1
            elif ")" in next:
                if "(" in opening_brackets_stack.pop():
                    #opening_brackets_stack.pop()
                    if i+1 == len(text):
                        return "Success"
                    else:
                        pass
                else:
                    return i + 1
            elif "}" in next:
                if "{" in opening_brackets_stack.pop():
                    if i+1 == len(text):
                        return "Success"
                    else:
                        pass
                else:
                    return i + 1
            elif "]" in next:
                if "[" in opening_brackets_stack.pop():
                    if i+1 == len(text):
                        return "Success"
                    else:
                        pass
                else:
                    return i + 1
            pass


def main():
    # print("Input text from file or input (F/I): ")
    # choice = input()

    text = input()
    mismatch = find_mismatch(text)

    if not mismatch:
        print("Success")
    else:
        print(mismatch)

    # if "F" in choice:
    #     # read from file
    #     file = open('0.txt', 'r')
    #     line = file.readline()
    #     mismatch = find_mismatch(line)
    #     print(mismatch)
    # elif "I" in choice:
    #     text = input()
    #     mismatch = find_mismatch(text)
    #     print(mismatch)
#         if "None" == mismatch:
#             print("Success")
#         else:
#             print(mismatch)
    # else:
    #     print("Error in input choice")


if __name__ == "__main__":
    main()
