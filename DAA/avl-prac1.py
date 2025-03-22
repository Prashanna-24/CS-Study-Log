class Node:
   def __init__(self,key):
      self.key = key
      self.left = None
      self.right = None
      self.height = 1

class AVL:
   def __init__(self):
      self.root = None
   
   def insert(self,key):
      self.root =  self._insert(self.root,key)

   def _insert(self,node,key):
      if not node:
         return Node(key)
      elif key < node.key:
         node.left = self._insert(node.left,key)
      elif key > node.key:
         node.right = self._insert(node.right,key)

      node.height = 1+max(self.getheight(node.left),self.getheight(node.right))
      balance = self.getbalance(node)

      if balance > 1 and key < node.left.key:
         return self.rightrotate(node)
      
      if balance < -1 and key > node.right.key:
         return self.leftrotate(node)
      
      if balance > 1 and key > node.left.key:
         node.left = self.leftrotate(node.left)
         return self.rightrotate(node)

      if balance < -1 and key < node.right.key:
         node.right = self.rightrotate(node.right)
         return self.leftrotate(node)
      
      return node
   def getheight(self,node):
      if node is None:
         return 0
      else:
         return node.height
      
   def getbalance(self,node):
      rh = self.getheight(node.right)
      lh = self.getheight(node.left)
      return lh - rh


   def rightrotate(self,node):
      a = node.left
      b = a.right
      a.right = node
      node.left = b

      node.height = 1+max(self.getheight(node.left),self.getheight(node.right))
      a.height = 1+max(self.getheight(a.left),self.getheight(a.right))

      return a
   
   def leftrotate(self,node):
      a = node.right
      b = a.left
      a.left = node
      node.right = b

      node.height = 1+max(self.getheight(node.left),self.getheight(node.right))
      a.height = 1+max(self.getheight(a.left),self.getheight(a.right))

      return a


   def preorder(self):
      self._preorder(self.root)

   def _preorder(self,node):
      if node is None:
         return 
      else:
         print(node.key,end=' ')
         self._preorder(node.left)
         self._preorder(node.right)

   def inorder(self):
      self._inorder(self.root)

   def _inorder(self,node):
      if node:
         self._inorder(node.left)
         print(node.key,end=' ')
         self._inorder(node.right)


   def delete(self,key):
      self.root = self._delete(self.root,key)

   def _delete(self,node,key):
      if node is None:
         return node
      elif key < node.key:
         node.left = self._delete(node.left,key)
      elif key > node.key:
         node.right = self._delete(node.right,key)
      else:
         if node.left is None:
               temp = node.right
               node = None
               return temp
         elif node.right is None:
               temp = node.left
               node = None
               return temp
         else:
               temp = self.findmin(node.right)
               node.key = temp.key
               node.right = self._delete(node.right,temp.key)

      if node is None:
         return node
      
      node.height = 1 + max(self.getheight(node.left),self.getheight(node.right))
      balance = self.getbalance(node)

      if balance > 1 and self.getbalance(node.left)>=0:
         return self.rightrotate(node)
      if balance < -1 and self.getbalance(node.right)<=0:
         return self.leftrotate(node)
      if balance > 1 and self.getbalance(node.left) < 0:
         node.left = self.leftrotate(node.left)
         return self.rightrotate(node)

      if balance < -1 and self.getbalance(node.right)>0:
         node.right = self.rightrotate(node.right)
         return self.leftrotate(node)
      
      return node

   def findmin(self,node):
      while node.left:
         node = node.left
      return node

arr=[40,20,10,25,30,22]
t=AVL()
for i in range(len(arr)):
   t.insert(arr[i])

t.preorder()
print()
t.inorder()
print()
t.delete(25)
t.preorder()
print()
t.inorder()