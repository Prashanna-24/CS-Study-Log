class stack:
   def __init__(self):
      # self.sz = 0
      self.top = -1
      self.stack = []

   def push(self,e):
      self.top += 1
      self.stack.append(e)

   def pop(self):
      if self.isempty():
         print("underflow")
      else:
         e = self.stack[self.top]
         self.top -= 1
         return e
      
   def isempty(self):
      if self.top == -1:
         return True
      else:
         return False
      
   def stacktop(self):
      if self.isempty():
         print("stack empty")
      else:
         return self.stack[self.top]
      
   def stacksize(self):
      return self.top+1 #also sz

class Node:
   def __init__(self,data):
      self.s1 = stack()
      self.s2 = stack()
      self.s1.push(data)
      self.next = None
      self.prev = None

class dll:
   def __init__(self):
      self.head = None
      self.tail = None

   def insertlast(self,data):
      new_node = Node(data)
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node
         new_node.prev = self.tail
         self.tail = new_node
   
   def deletelast(self):
      self.tail.prev.next = None
      self.tail = self.tail.prev

   def replace(self,data1,data2):
      current_node = self.head
      while(current_node.s1.stacktop() != data1):
         current_node = current_node.next
      current_node.s1.push(data2)

   def undo(self,data):
      current_node = self.head
      while(current_node.s1.stacktop() != data):
         current_node = current_node.next
      current_node.s2.push(current_node.s1.pop())
      
   def redo(self,data):
      current_node = self.head
      while(current_node.s1.stacktop() != data):
         current_node = current_node.next
      current_node.s1.push(current_node.s2.pop())

   def printfromfirst(self):
      current_node = self.head
      print("dll elements: ")
      while(current_node != None):
         print(current_node.s1.stacktop(),end=' ')
         current_node = current_node.next
      print()

mydll = dll()
mydll.insertlast("hello")
mydll.insertlast("nigga")
mydll.insertlast("how")
mydll.printfromfirst()
mydll.insertlast("you")
mydll.replace("nigga","karupa")
mydll.printfromfirst()
mydll.undo("karupa")
mydll.printfromfirst()
mydll.redo("nigga")
mydll.printfromfirst()