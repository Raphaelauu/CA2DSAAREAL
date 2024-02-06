# Authors: Irfan Nasim & Raphael Lau
# Admission Number: 2201816 & ???????
# Class: DAAA/FT/2B/07 

# Define a class for a binary tree node
class BinaryTree:
    # Initialize a binary tree node with a key and optional left and right children
    def __init__(self, key, leftTree=None, rightTree=None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    # Set the key of this node
    def setKey(self, key):
        self.key = key

    # Get the key of this node
    def getKey(self):
        return self.key

    # Get the left child of this node
    def getLeftTree(self):
        return self.leftTree

    # Get the right child of this node
    def getRightTree(self):
        return self.rightTree

    # Insert a new node as the left child of this node
    def insertLeft(self, key, parent_tree_id=None):
            if self.leftTree == None:
                self.leftTree = self.__class__(key, parent_tree_id=parent_tree_id)
            else:
                t = self.__class__(key, parent_tree_id=parent_tree_id)
                self.leftTree, t.leftTree = t, self.leftTree

    # Insert a new node as the right child of this node
    def insertRight(self, key, parent_tree_id=None):
        if self.rightTree == None:
            self.rightTree = self.__class__(key, parent_tree_id=parent_tree_id)
        else:
            t = self.__class__(key, parent_tree_id=parent_tree_id)
            self.rightTree, t.rightTree = t, self.rightTree

    # Print the keys of the nodes in this binary tree in inorder traversal
    def printInorder(self, level):
        # First, print the keys in the right subtree
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)
        
        # Then, print the key of this node
        print(str(level*'.') + str(self.key))
        
        # Finally, print the keys in the left subtree
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)