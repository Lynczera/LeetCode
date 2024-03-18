'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]

we can create a hm that will store the first instance of the word and the anagrams of it. 
when storing, we need to have the character ordered and make sure to track the indexes of the anagrams

'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = dict()

    for i in range(len(strs)):
        curr_char_ordered = "".join(sorted(strs[i]))
        if curr_char_ordered in anagrams:
            anagrams[curr_char_ordered].append(i)
        else:
            anagrams[curr_char_ordered] = [i]
    
    result = []
    for key in anagrams:
        curr_anagrams = anagrams[key]
        curr_arr = []
        for index in curr_anagrams:
            curr_arr.append(strs[index])
        result.append(curr_arr)

    return result

