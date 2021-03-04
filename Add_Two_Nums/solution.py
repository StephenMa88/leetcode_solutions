# attempted in 2021
# 76ms, 14.6 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lnToList(self, listNode, lnlist =[]):
        lnlist.append(listNode.val)
        if listNode.next is not None:
            self.lnToList(listNode.next, lnlist)
        return lnlist
    
    def listToLN(self, Nlist, i=0):
        lnode = ListNode(Nlist[i])
        
        while i < len(Nlist):
            try:
                i += 1
                nnode = ListNode(Nlist[i])
                nnode.next = lnode
                lnode = nnode
            except IndexError:
                return lnode
        return lnode
        
    def addMore(self, listn, num):
        zeros = []
        print(num)
        for x in range(num):
            zeros.append(0)
        result = listn + zeros
        return result
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create listnode to list
        list1 = self.lnToList(l1, lnlist =[])
        #print(list1)
        list2 = self.lnToList(l2, lnlist =[])
        #print(list2)
        
		# if one list longer than the other
        if len(list1) > len(list2):
            list2 = self.addMore(list2, len(list1) - len(list2))
        elif len(list2) > len(list1):
            list1 = self.addMore(list1, len(list2) - len(list1))
        #print(list1)
        #print(list2)
        
        total = 0
        for x in range(len(list1)):
            #print("b {} {} {}, {}".format(total,list1[x], list2[x], 10**x))
            total = total + ((list1[x]+list2[x])*(10**x))
            #print("a {} {} {}".format(total,list1[x], list2[x]))
        
        flist = []
		# Number to list
        for y in str(total):
            flist.append(int(y))
        #print(flist)
        
        result = self.listToLN(flist)
        
        #print(result)
        return result

# attempted in 2020
# 88ms, 14 MB
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLL:
    # what the problem gives me is a list node but not a singly linked list. They nodes are not             connected.
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def lltoString(self, llist):
        str_val = []
        str_re = ""
        
        cur_head = llist
        
        while cur_head is not None:
            str_val.append(cur_head.val)
            cur_head = cur_head.next
            
        for x in str_val[::-1]:
            str_re += str(x)
        
        return str_re

class Solution:
    # From SSL -> list --> reverse list --> string --> int
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = SingleLL()
        n2 = SingleLL() 
        n3 = SingleLL()
        
        s_n1 = n1.lltoString(l1)
        s_n2 = n2.lltoString(l2)
        #print("{} \n {}".format(s_n1, l2)
        
        s_n3 = int(s_n1) + int(s_n2)
        #print(s_n3)
        
        l_n3 = []
        for x in str(s_n3):
            l_n3.append(int(x))
        
        l3 = ListNode(l_n3[0])
        #print(l3)
        #print(l_n3)
        for x in range(len(l_n3)):
            if x != 0:
                llist = ListNode(l_n3[x])
                llist.next = l3
                l3 = llist
            
        return l3
"""
