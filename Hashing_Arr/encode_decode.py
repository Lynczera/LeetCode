from typing import List

"""

to indicate each string, we are going to add a num and a "#" 
this will indicate how long the next word is. 
"""


def encode(strs) -> str:
    encoded = ""

    for word in strs:
        encoded += str(len(word))
        encoded += "#"
        encoded += word

    return encoded


def decode(s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        result += [s[j + 1 : j + 1 + length]]
        i = j + 1 + length
    return result


test = ["neet", "code"]

print(encode(test))
print(decode(encode(test)))
