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

    
    '''INSERT METHOD WHICH CALLS _insert
       input: value to be inserted
       output: none
    '''
    def insert(self, data):
        if self.root is None:                                       #If the root node is empty
            self.root = Node(data)                                  #create root node using data given
        else:
            self._insert(data, self.root)                           #ELSE run the _insert function with the root node
                                                                    #as the current node
    '''INSERT METHOD
       input: data, current node
       output: none
    '''
    def _insert(self, data, cur_node):
        if data < cur_node.data:                                    #if data < value of current node
            if cur_node.left is None:                               #if left child node is empty
                cur_node.left = Node(data)                          #create node where its value is data
            else:
                self._insert(data, cur_node.left)                   #ELSE rerun with left child node as current node
        elif data > cur_node.data:                                  #if data > value of current node
            if cur_node.right is None:                              #if right child node is empty
                cur_node.right = Node(data)                         #create node where its value is data
            else:
                self._insert(data, cur_node.right)                  #ELSE rerun with right child node as current node
        else:
            print("Value already present in tree")                  #ELSE print to screen

            
    '''REMOVE METHOD FOR BINARY TREE
       input: target value
       output: True if target removed, False if not'''
    def remove(self, target):
        if self.root == None:                                       #if root node is empty
            return False                                            #return False
        elif self.root.data == target:                              #if root node is the target
            if self.root.left == None and self.root.right == None:  #if left and right child are not present
                self.root = None                                    #remove root node
            elif self.root.left and self.root.right == None:        #if only left child is present
                self.root = self.root.left                          #remove root node and left child becomes root node
            elif self.root.left == None and self.root.right:        #if only right child is present
                self.root = self.root.right                         #right child becomes root node
            elif self.root.left and self.root.right:                #if both left and right child are present
                self.if_left_and_right(self.root)                   #go to function which deals with this case
    
        parent = None
        node = self.root                                            #store root node in variable "node"

        while node and node.data != target:                         #while node is not empty and node not equal to target
            parent = node                                           #store node in varable parent
            if target < node.data:                                  #if target < value of node
                node = node.left                                    #move to left child node
            elif target > node.data:                                #if target > value of node
                node = node.right                                   #move to right child node

        if node == None or node.data != target:                     #Case1 Target Not Found
            return False
        
        elif node.left == None and node.right == None:              #Case 2 Target has no children
            if target < parent.data:                                #if target < value of parent node of target
                parent.left = None                                  #remove left child of parent
            else:
                parent.right = None                                 #remove right child of parent
            return True                                             #return True to show target has been removed
        
        elif node.left and node.right == None:                      #Case 3 Target has left child only
            if target < parent.data:                                #if target < value of parent node of target
                parent.left = node.left                             #parents left child becomes targets left child
            else:
                parent.right = node.left                            #parents right child becomes targets left child
            return True                                             #return True to show target has been removed
        
        elif node.right and node.left == None:                      #Case 4 Target has right child only
            if target > parent.data:                                #if target > value of parent node of target
                parent.right = node.right                           #parents right child becomes targets right child
            else:
                parent.left = node.right                            #parents left child becomes targets right child
            return True
        
        else:                                                       #Case 5 Target has left and right children
            self.if_left_and_right(node)                            #call function to that handles left and right children

    '''METHOD TO HANDLE BOTH LEFT AND RIGHT CHILDREN
       input: target node
    '''
    def if_left_and_right(self, node):#Self not in pesudocode       #Called if delete node wether root or otherwise
        delNodeParent = node                                        #has left and right children
        delNode = node.right

        while delNode.left:
            delNodeParent = delNode
            delNode = delNode.left
        
        node.data = delNode.data

        if delNode.right:
            if delNodeParent.data > delNode.data:
                delNodeParent.left = delNode.right
            else:
                delNodeParent.right = delNode.right
            
        else:
            if delNode.data < delNodeParent.data:
                delNodeParent.left = None
            else:
                delNodeParent.right = None
    #--------------My Code Ends----------------------------#
    
    def display(self, cur_node):
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
'''bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)'''

bst.display(bst.root)
bst.remove(10)
bst.display(bst.root)



