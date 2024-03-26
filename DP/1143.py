
"""

Longest common subsequence 

string x and y / solution k

first backward 
curr x or curr y can be equal to the curr solution k. -> we decrease both and add the curr char to the solution 

if cur x is not, we move it backward 
if curr y is not, we move it backward

second forward
the base case is either one of the curr substrings is len 0. Then we can ensure the value is false in the dp arr

then, if xn == ym, we set the curr xi,ji to be the previous sub solution + 1(curr) 

if xn != ym -> either xn is not in the solution or ym is not in the solution

but both xn and ym came from a branch that has a solution -> we choose the max between then. 

"""

def print_table_opt(table):
    for i in range(len(table) - 1, -1, -1):
        curr = []
        for j in range(len(table[i])):
            curr.append(table[i][j])
        print(curr)


def lcs(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if text1[j - 1] == text2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(text2)][len(text1)]
