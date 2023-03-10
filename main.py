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
            opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    # Printing answer, write your code here
    file = input()
    if "F" in file:
        file = input()
        with open(file, "r", encoding="ISO-8859-1") as file:
            read=file.read()
        mismatch = find_mismatch(read)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    elif "I" in file:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    else:
        mismatch = find_mismatch(file)
        print(mismatch)

main()
