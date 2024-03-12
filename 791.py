'''
we can count the # of each char in string and put in a hashmap

then, we create the result by looping over order, and grabbing the keys in the correct order
as we grab the keys, we can also remove since there will be elements that wont be in the order var

finally, we just need to go over the remainder characters in the dict and add to the result

'''


def customSortString(order: str, s: str) -> str:
    aux_dict = dict()

    for char in s:
        if char in aux_dict.keys():
            aux_dict[char] +=1
        else:
            aux_dict[char] = 1

    result = ""
    for char in order:
        if char in aux_dict.keys():
            currchar = char*aux_dict[char]
            result += currchar
            aux_dict.pop(char)
    for remainder in aux_dict.keys():
        rm = remainder * aux_dict[remainder]
        result += rm

    return result
    