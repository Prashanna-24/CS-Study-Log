#https://youtube.com/playlist?list=PLVkDztYhxUGH9AubH9hLy_JYam8EZ9VKs&si=2REdzqp9M39j28xe

class Node:
   def __init__(self,value):
      self.data = value
      self.left = None
      self.right = None
      self.parent = None

class Heap:
   def __init__(self):
      self.root = None
   def addElement(self,value):
      if not self.root:
         self.root = Node(value)
      else:
         self.add_recursively(value,self.root)
   def add_recursively(self,data,node):
      if not node.left:
         node.left = Node(data)
         node.left.parent = node
         self.heapify_up(node.left)
      elif not node.right:
         node.right = Node(data)
         node.right.parent = node
         self.heapify_up(node.right)
      else:
         if self.count_node(node.left) <= self.count_node(node.right):
            self.add_recursively(data,node.left)
         else:
            self.add_recursively(data,node.right)

   def count_node(self,node):
      if not node:
         return 0
      return 1+ self.count_node(node.left)+ self.count_node(node.right)
   
   def heapify_up(self,node):
      while node and node!=self.root:
         if node.data<node.parent.data:
            node.data,node.parent.data = node.parent.data,node.data
            node = node.parent
         else:
            break

   def extract_min(self):
      if not self.root:
         print("heap empty")
         return
      min = self.root.data
      last_node_data = self.removeLastNode()
      if last_node_data:
         self.root.data = last_node_data
         self.heapify_down(self.root)
      else:
         self.root = None
      return min

   def removeLastNode(self):
      q = []
      q.append(self.root)
      while len(q)!=0:
         curr_node = q.pop(0)
         if curr_node.left:
            q.append(curr_node.left)
         if curr_node.right:
            q.append(curr_node.right)
         last_node = curr_node
      last_node_data = last_node.data
      last_node = None
      return last_node_data
   
   def heapify_down(self,node):
      while node:
         small_node = node
         if node.left and node.left.data<small_node.data:
            small_node = node.left
         if  node.right and node.right.data<small_node.data:
            small_node = node.right
         if small_node != node:
            node.data,small_node.data = small_node.data,node.data
            node = small_node
         else:
            break



myheap = Heap()
myheap.addElement(10)
myheap.addElement(7)
myheap.addElement(6)
myheap.addElement(5)
myheap.addElement(4)
# myheap.addElement(66)
# myheap.addElement(77)

print(myheap.root.data)
print(myheap.root.left.data)
print(myheap.root.right.data)
print(myheap.root.left.left.data)
# print(myheap.root.left.right.data)
print(myheap.root.right.left.data)
# print(myheap.root.right.right.data)
print(myheap.extract_min())
print(myheap.root.data)