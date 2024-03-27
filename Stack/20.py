"""

we can put open brackets in a stack. once we find a closing one, we check if the 
top of the stack has a openning one. 
"""


def isValid(self, s: str) -> bool:
    stack = []

    for letter in s:
        if letter == "{" or letter == "(" or letter == "[":
            stack.append(letter)
        else:
            if len(stack) == 0:
                return False

            if letter == "}":
                if stack.pop() == "{":
                    continue
                else:
                    return False
            elif letter == ")":
                if stack.pop() == "(":
                    continue
                else:
                    return False
            else:
                if stack.pop() == "[":
                    continue
                else:
                    return False
    return len(stack) == 0
