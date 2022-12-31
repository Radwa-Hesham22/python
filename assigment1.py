class queue:
   def __init__(self):
      self.values=[]
   def is_empty(self):
         if self.values == []:
            print("empty")
            return True
         else:
           return False
   def insert(self,value):
         self.values.append(value)
   def pop(self):
         if self.values==[]:
            print("warning: the queue is empty")
            return None
         else:
            x=self.values.pop(0)
            return x
   def display(self):
         for i in self.values:
            print(i)


q=queue()
q.insert(12)
q.insert(15)
q.display()
q.pop()
q.display()
q.pop()
q.pop()
q.is_empty()



  



   