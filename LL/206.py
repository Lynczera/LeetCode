

'''
1->2->3

curr = 1
next = 2

save 3 
point 2 to 1
set curr to 2
set next to 3 

'''


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    if head == None:
        return None
    
    if head.next == None:
        return head


    curr = head        
    nextcurr = curr.next
    curr.next = None

    while nextcurr != None:
        temp = nextcurr.next
        nextcurr.next = curr
        curr = nextcurr
        nextcurr = temp
    return curr