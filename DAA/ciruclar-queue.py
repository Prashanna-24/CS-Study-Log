class circularqueue:
   def __init__(self,mxsize):
      self.q = [None] * mxsize
      self.front = 0
      self.rear = 0
      self.mxsize = mxsize
   def enqueue(self,value):
      if self.isfull():
         print("queue full")
      else:
         self.q[self.rear] = value
         self.rear = (self.rear + 1)%self.mxsize

   def dequeue(self):
      if self.isempty():
         print("queue empty")
      else:
         self.q[self.front] = None
         self.front = (self.front + 1) % self.mxsize

   def qfront(self):
      return self.q[self.front]

   def isempty(self):
      if self.qsize() == 0:
         return True
      else:
         return False
   def isfull(self):
      if self.qsize() == self.mxsize:
         return True
      else:
         return False
   def qsize(self):
      if self.front <= self.rear:
         return (self.rear - self.front)
      else:
         return (self.mxsize-(self.front - self.rear))
   def printq(self):
      print("cqueue: ")
      i = self.front
      while i!=self.rear:
         print(self.q[i],end=' ')
         i = (i+1)%self.mxsize
      print()

'''
1-nq 2-dq 3-fr 4-print 5-exit
'''
myq = circularqueue(6)
choice = int(input("choice: "))
while True:
   if choice == 1:
      element = int(input("enter the element: "))
      myq.enqueue(element)
   elif choice == 2:
      myq.dequeue()
   elif choice == 3:
      print(myq.qfront())
   elif choice == 4:
      myq.printq()
   elif choice == 5:
      print("exiting")
      break
   else:
      print("invalid")
   choice = int(input("choice: "))