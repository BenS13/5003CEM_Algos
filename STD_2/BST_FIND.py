""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None
    
    '''FIND METHOD ITERATIVE
       input: binary tree, target(value to find)
       output: True(if found), False(if not found), None
       Implements iterative find function in the Binary Tree Class
    '''
    def find_i(self, target):
        if self.root == None:            #If there is no binary tree
            return None                  #return None
        cur_node = self.root             #Set cur_node to the root node
        while cur_node != None:          #While current node is not empty
            if cur_node.data == target:  #If the value of the current node is equal to the target
                return True              #return True
            elif cur_node.data > target: #If value of current node is > target
                cur_node = cur_node.left #Current node becomes left child node
            else:
                cur_node = cur_node.right#Move to right child node if current node value < target
        return False                     #Return False if the target is not found
    
    
    
    '''FIND METHOD RECURSIVE
       input: binary tree, target
       output: True, False, None
       Implements recursive function in the Binary Tree Class
    '''
    def find_r(self, target):
        if self.root:                                  #If root node is not empty
            if self._find_r(target, self.root):        #If _find_r returns True return True
                return True
            return False                               #If _find_r returns False return False
        else:
            return None                                #If root node is empty return None

    def _find_r(self, target, cur_node):               #Pass through target and current node
        if target > cur_node.data and cur_node.right:  #If target > value of current node AND right child
                                                       #node exists
            return self._find_r(target, cur_node.right)#Rerun _find_r where target = target AND 
                                                       #cur_node = cur_node.right
        elif target < cur_node.data and cur_node.left: #If target < value of current node AND left child
                                                       #node exists
            return self._find_r(target, cur_node.left) #Rerun _find_r where target=target AND
                                                       #cur_node = cur_node.left
        if target == cur_node.data:                    #If target is equal to the value of the current node
            return True                                #_find_r returns True which subsiqently makes find_r
                                                       #return True


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        if cur_node == None:
            print("Empty Tree")
            return None
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):

        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
'''bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)'''

bst.display(bst.root)
print(bst.find_i(20))
print(bst.find_r(20))



