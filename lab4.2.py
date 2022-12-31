class QueueOutOfRangeException(Exception):
  pass
class queue:
  x={}
  def __init__(self,name,size):
    super().__init__() 
    self.values=[]
    self.name=name
    self.size=size
    queue.x[self.name]=self.values

  def is_empty(self):
         if self.values == []:
            print("empty")
            return True
         else:
           return False
  def insert(self,value):
    if len(self.values)==self.size :
      raise QueueOutOfRangeException("the queue is full")
    else:
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

q=queue("y",3)
q.insert(12)
q.insert(15)
q.insert(11)
q.display()
print(queue.x)
       



    
   
