
'''
2 pointers, one on each end. Move then until middle and check as you move

'''

def isPalindrome(self, s: str) -> bool:
    i=0
    j=len(s)-1

    while i<=j:
        curri = s[i].lower()
        currj = s[j].lower()

        if not curri.isalnum():
            i+=1 
            continue
        if not currj.isalnum():
            j-=1
            continue
        
        if curri == currj:
            i+=1
            j-=1
        else:
            return False
        
    return True