import math
from collections import deque

class BinaryTree:

    class node:
        def __init__(self):
            self.element = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.root=None
        self.sz=None
    def inorderTraverse(self,root):
        if(root):
            self.inorderTraverse(root.leftchild)
            print(root.element,end=" ")
            self.inorderTraverse(root.rightchild)

    def preorderTraverse(self,root):    
        if(root):
            print(root.element,end=" ")
            self.preorderTraverse(root.leftchild)
            self.preorderTraverse(root.rightchild)
    def postorderTraverse(self,root):
        if(root):
            self.postorderTraverse(root.leftchild)
            self.postorderTraverse(root.rightchild)
            print(root.element,end=" ")
    def findDepth(self,x):
        b=self.depth(self.root,x)
        return b

    def depth(self,root,x):
        if(root==None):
            return -1
        d1=-1
        if root==x:
            return d1+1
        d1=self.depth(root.leftchild,x)
        if d1 >= 0:
            return d1 + 1
        d1=self.depth(root.rightchild,x)
        if d1 >= 0:
            return d1 + 1
        return d1   
        
    def height(self,root,x):
        global h
        if(root==None):
            return -1

        k1=self.height(root.leftchild,x)
        k2=self.height(root.rightchild,x)
        a=max(k1,k2)+1
        if(root==x):
            h=a
        return a
    def findHeight(self,x):
        global h
        self.height(self.root,x)
        return h

    def levelorderTraverse(self,root):
        p = self.findHeight(self.root)
        for i in range(1, p+2):
            self.printCurrentLevel(self.root,i)
    def printCurrentLevel(self,root,level):
        if root is None:
            return
        if level == 1:
            print(root.element, end=" ")
        elif level > 1:
            self.printCurrentLevel(root.leftchild, level-1)
            self.printCurrentLevel(root.rightchild, level-1) 
    
    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz=len(nodelist)
        return nodelist
    
    
    
    
    
   
    

#Driver code - DO NOT EDIT
def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "IN"):
            tree.inorderTraverse(tree.root)
            print()
        elif (operation[0] == "PR"):
            tree.preorderTraverse(tree.root)
            print()
        elif (operation[0] == "PO"):
            tree.postorderTraverse(tree.root)
            print()
        elif (operation[0] == "L"):
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == "D"):
            pos = int(operation[1])
            print(tree.findDepth(nlist[pos]))
        elif (operation[0] == "H"):
            pos = int(operation[1])
            print(tree.findHeight(nlist[pos]))
        inputs -= 1

if __name__ == '__main__':
    main()

