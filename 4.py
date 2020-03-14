#Python program to calculate perimeter and area of square 
#Defining class square 
class square:  
   
   
   #Accepting input from user for calculating area of square  
    def CalculateArea(self):
        print("Enter side")
        self.s=float(input())
        area=self.s*self.s
        return(area)
      
    
  #Calculating perimeter of square
    def CalculatePerimeter(self):
      perimeter=4*self.s
      return(perimeter)
   
   
   
   
#Defining object of the class square.
c=square()
#Calling the fuction
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of square is=%f"%(x))
print("Perimeter of square is=%f"%(y))
