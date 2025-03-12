#https://youtube.com/playlist?list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&si=Srp8bBkbC6seT_s6

class Node():
   def __init__(self,value):
      self.data = value
      self.right = None
      self.left = None

class BinaryTree():
   def __init__(self,rootvalue):
      self.root = Node(rootvalue)

   def height(self,node,x):
      global required_height
      if node is None:
         return -1
      left_height = self.height(node.left,x)
      right_height = self.height(node.right,x)
      h = 1+ max(left_height,right_height)
      if node.data == x:
         required_height = h
      return h
   def height_of_node(self,x):
      global required_height
      self.height(self.root,x)
      return required_height
   
   def findParent(self,root, node):
      if root is None:
         return None
      if (root.left and root.left.data == node) or (root.right and root.right.data == node):
         return root
      # Check recursively in left and right subtrees
      left_parent = self.findParent(root.left, node)
      if left_parent:
         return left_parent
      right_parent = self.findParent(root.right, node)
      if right_parent:
         return right_parent
      return None
   
   def printAncestors(self,root, target):
      if root == None:
         return False
      if root.data == target:
         return True
      # If target is present in either left or right subtree then print this node
      if (self.printAncestors(root.left, target) or self.printAncestors(root.right, target)):
         print(root.data,end=' ')
         return True

      return False
   
   def preorderTraverse(self,start): #root->left->right
      if(start):
         print(start.data,end=" ")
         self.preorderTraverse(start.left)
         self.preorderTraverse(start.right)

   def inorderTraverse(self,start): #left->root->right
      if(start):
         self.inorderTraverse(start.left)
         print(start.data,end=" ")
         self.inorderTraverse(start.right)
   def inorderTraverse_itr(self):
      stack = []
      # result = []
      current_node = self.root
      while stack or current_node:
         while current_node:
            stack.append(current_node)
            current_node = current_node.left
         current_node = stack.pop()
         print(current_node.data,end=" ")
         # result.append(current_node.data)
         current_node = current_node.right
      return

   def postorderTraverse(self,start): #left->right->root
      if(start):
         self.postorderTraverse(start.left)
         self.postorderTraverse(start.right)
         print(start.data,end=" ")

   def levelordertraversal(self):
      q = []
      q.append(self.root)
      while(len(q)):
         temp = q.pop(0)
         print(temp.data,end=' ')
         if temp.left:
            q.append(temp.left)
         if temp.right:
            q.append(temp.right)

   def ifNodeExists(self,xnode,key):
      if xnode == None:
         return False
      if xnode.data == key:
         return True
      return self.ifNodeExists(xnode.left,key) or self.ifNodeExists(xnode.right,key)

mytree = BinaryTree(11)
mytree.root.left = Node(22)
mytree.root.right = Node(33)
mytree.root.left.left = Node(44)
mytree.root.left.right = Node(55)
mytree.root.right.left = Node(66)
mytree.root.right.right = Node(77)
mytree.root.right.right.right = Node(88)
# print(mytree.height(mytree.root.right.right))
# mytree.preorderTraverse(mytree.root)
# print()
# mytree.inorderTraverse(mytree.root)
# print()
# mytree.inorderTraverse_itr()
# mytree.postorderTraverse(mytree.root)
# print(mytree.ifNodeExists(mytree.root,88))
# mytree.findParent(mytree.root,66, -1)
# p = mytree.findParent(mytree.root,66)
# print(p.data)
# mytree.printAncestors(mytree.root,88)
# print(mytree.height_of_node(77))
mytree.levelordertraversal()
'''

# Python3 implementation of tree using array
# numbering starting from 0 to n-1.
tree = [None] * 10


def root(key):
	if tree[0] != None:
		print("Tree already had root")
	else:
		tree[0] = key


def set_left(key, parent):
	if tree[parent] == None:
		print("Can't set child at", (parent * 2) + 1, ", no parent found")
	else:
		tree[(parent * 2) + 1] = key


def set_right(key, parent):
	if tree[parent] == None:
		print("Can't set child at", (parent * 2) + 2, ", no parent found")
	else:
		tree[(parent * 2) + 2] = key


def print_tree():
	for i in range(10):
		if tree[i] != None:
			print(tree[i], end="")
		else:
			print("-", end="")
	print()


# Driver Code
root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()
'''