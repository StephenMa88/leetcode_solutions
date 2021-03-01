tion for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

#Sample output: TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}} 

class Solution:
    def __init__(self):
        #self.tree_list = []
        self.tree_dict = {}
        self.counter = 0

    def treeToDict(self, treenode):
        # check if this key exists
        if self.tree_dict.get(self.counter):
            self.tree_dict[self.counter].append(treenode.val)
        else:
            self.tree_dict[self.counter]=[treenode.val]
        # to signify moving down the tree.
        self.counter+=1

        # goes down and print all from left side
        if treenode.left:
            self.treeToDict(treenode.left)

        # then go down the right side but also left side first
        if treenode.right:
            self.treeToDict(treenode.right)
        # to signify moving up the tree
        self.counter-=1
    """
    def treeToList(self, treenode):
        # List method
        self.tree_list.append(treenode.val)
        
        # goes down and print all from left side
        if treenode.left:
            self.treeToList(treenode.left)

        # then go down the right side but also left side first
        if treenode.right:
            self.treeToList(treenode.right)
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # if empty
        if not root:
            return []

        # Get node tree as list or dict
        self.treeToDict(root)
        
        #print(len(self.tree_dict))
        # if len one then
        if len(self.tree_dict) == 1:
            return [self.tree_dict[0]]

        output = []
        for x in self.tree_dict.values():
            output.append(x)

        #print(self.tree_dict)
        return output
          
        
        """
        #Old code - used when trying to solve using list
        #self.treeToList(root)
        output = [[self.tree_list[0]]]
        try:
            for x in range(1, len(self.tree_list)+1):
                #print(x)
                if x%2 == 0:
                    output.append([self.tree_list[x-1], self.tree_list[x]])
        except IndexError:
            output.append([self.tree_list[x-1]])
        
        #return self.tree_list
        """                  
