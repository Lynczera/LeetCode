'''
count frequency of each char in each word and put in a dict 

compare the 2 dict to see if they are equal = check anagram 
'''

def isAnagram(s: str, t: str) -> bool:
    freq_s = dict()
    freq_t = dict()

    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    return freq_s == freq_t


