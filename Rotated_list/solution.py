# attempted in 2021
# 40ms, 14.4 MB 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lnToList(self, listnode):
        output = listnode
        lnodeToList = []
        while True:
            lnodeToList.append(output.val)
            output = output.next
            if output is None:
                return lnodeToList
                
    def listToLN(self, list):
        # initiate the last link in the list
        node = ListNode(list[0])
        # loop through the list
        for i, x in enumerate(list):
            if i == 0:
                continue
            # create linked list from value
            second = ListNode(x)
            # make sure new linked list is pointing to the last node
            second.next = node
            # reset node to be holding the updated linked list
            node = second
        return node
            
        
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # if head is None
        if head is None:
            return head
        
        # create list out of ListNode
        list_nodes = self.lnToList(head)
        #print(list_nodes)
        rotated_list = []
            
        # rotate list to right k times
        for x in range(len(list_nodes)):
            new_index = (x + k) % len(list_nodes)
            rotated_list.insert(new_index, list_nodes[x])
        #print(rotated_list)
        
        # send it in in reverse order to create end first
        output = self.listToLN(rotated_list[::-1])
        return output
        
