class stack:
   def __init__(self,size):
      # self.sz = 0
      self.maxsz = size
      self.top = -1
      self.stack = []
      for i in range(size):
         self.stack.append(None)

   def push(self,e):
      if self.isfull():
         print("overflow")
      else:
         self.top += 1
         self.stack[self.top] = e

   def pop(self):
      if self.isempty():
         print("underflow")
      else:
         e = self.stack[self.top]
         self.top -= 1
         return e

   def isfull(self):
      if self.top+1==self.maxsz:
         return True
      else:
         return False
      
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
   
   def stackprint(self):
      if self.isempty():
         print("empty stack")
      else:
         for i in range(self.top+1):
            print(self.stack[i],end=" ")
         print('\n')

st = stack(5)
st.push(11)
st.push(22)
st.push(33)
st.stackprint()
st.pop()
st.stackprint()

