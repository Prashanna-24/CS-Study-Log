class Node:
   def __init__(self, name, size=0):
      self.name = name
      self.size = size
      self.left = None
      self.right = None

class Binarytree:
   def __init__(self):
      self.root = None

   def find_node_levelorder(self, x):
      q = [self.root]
      while q:
         temp = q.pop(0)
         if temp.name == x:
               return temp
         if temp.left:
               q.append(temp.left)
         if temp.right:
               q.append(temp.right)

   def addnode_under(self, node, target):
      f = self.find_node_levelorder(target)
      if f.left and f.right:
         print("directory full!!!")
      elif f.left and not f.right:
         f.right = node
         print(f"added {node.name} under {f.name}")
      else:
         f.left = node
         print(f"added {node.name} under {f.name}")

   def ancestors(self, xnode, target, ancestor_list):
      if not xnode:
         return False
      if xnode.name == target:
         return True
      if self.ancestors(xnode.left, target, ancestor_list) or self.ancestors(xnode.right, target, ancestor_list):
         ancestor_list.append(xnode.name)
         return True
      return False

   def printPath(self, xnode, target):
      ancestor_list = []
      self.ancestors(xnode, target, ancestor_list)
      print(ancestor_list)

   def inorder(self,node):
      if(node):
         self.inorder(node.left)
         print(node.name,end=" ")
         self.inorder(node.right)

mytree = Binarytree()
mytree.root = Node("dir1", 10)
new = Node("dir2", 10)
f = mytree.addnode_under(new, "dir1")
new = Node("dir3", 10)
f = mytree.addnode_under(new, "dir1")
new = Node("dir4", 10)
f = mytree.addnode_under(new, "dir2")
new = Node("dir5", 10)
f = mytree.addnode_under(new, "dir2")
mytree.printPath(mytree.root, "dir5")
mytree.inorder(mytree.root)