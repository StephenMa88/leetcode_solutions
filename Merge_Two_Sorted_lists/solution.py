# attempted in 2021
# 44ms, 14.5 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lnToList(self, ln, result=[]):
        result.append(ln.val)
        if ln.next is not None:
            self.lnToList(ln.next, result)
        return result
    
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return l1
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        list1 = self.lnToList(l1, result=[])
        list2 = self.lnToList(l2, result=[])
        
        twolist = sorted(list1 + list2)[::-1]
        
        print(twolist)
        
        output = ListNode(twolist[0])
        for x in twolist[1:]:
            sub = ListNode(x)
            sub.next = output
            output = sub
        
        return output

# attempt in 2020
# 40ms, 13.9 MB
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Singll:
    def __init__(self):
        pass
        
    def go_thur(self, lnode):
        node_list = []
        
        curr_head = lnode
        while curr_head:
            node_list.append(curr_head.val)
            curr_head = curr_head.next
        
        return node_list
    
    def listToNode(self, output_list):
        output = ListNode(output_list[0]) 
        for x in output_list[1:]:
            out_2 = ListNode(x)
            out_2.next = output
            output = out_2
        
        return output

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = Singll()
        n2 = Singll()
        n3 = Singll()
        
        list_n1 = n1.go_thur(l1)
        list_n2 = n2.go_thur(l2)        
        #print(list_n1)
        list_output = list_n1 + list_n2
        list_output.sort()
        #print(list_output)
        
        if list_output:
            output = n3.listToNode(list_output[::-1])
        else: 
            empty = ListNode("")
            return empty
        
        return output
"""
