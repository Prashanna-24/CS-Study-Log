class Node:
   def __init__(self,data):
      self.data = data
      self.next = None
      self.prev = None

class dll:
   def __init__(self):
      self.head = None
      self.tail = None

   def insertfirst(self,data):
      new_node = Node(data)
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         new_node.next = self.head
         self.head.prev = new_node
         self.head = new_node

   def insertlast(self,data):
      new_node = Node(data)
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node
         new_node.prev = self.tail
         self.tail = new_node
   
   def deletefirst(self):
      #add constraint for empty
      self.head.next.prev = None
      self.head = self.head.next
   def deletelast(self):
      self.tail.prev.next = None
      self.tail = self.tail.prev
         
   def printfromfirst(self):
      current_node = self.head
      print("dll elements: ")
      while(current_node != None):
         print(current_node.data,end=' ')
         current_node = current_node.next
      print()

'''
1-insertfirst 2-insertlast 3-printfromfirst
'''

mydll = dll()
choice = int(input("choice: "))
while True:
   if choice == 1:
      element = int(input("enter the element: "))
      mydll.insertfirst(element)
   elif choice == 2:
      element = int(input("enter the element: "))
      mydll.insertlast(element)
   elif choice == 3:
      mydll.deletefirst()
   elif choice == 4:
      mydll.deletelast()
   elif choice == 5:
      mydll.printfromfirst()
   elif choice == 6:
      print("exiting")
      break
   else:
      print("invalid")
   choice = int(input("choice: "))