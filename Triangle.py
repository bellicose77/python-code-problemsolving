class Triangle:
   def __init__(self,a,b,c):
    self.left=a
    self.right=b
    self.height=c

   def premiter (self):
    result = self.left+self.right+self.height
    return result
triangleOne = Triangle(5,6,7)
x=triangleOne.premiter()
print(x)