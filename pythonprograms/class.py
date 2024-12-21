import math
class Shape:
    def area(self):
        raise NotImplementedError("this method is inherited")
    def perimeter(self):
        raise NotImplementedError("this method is inherited ")

class Circle(Shape):

    def init(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)  
    def perimeter(self):
        return 2*math.pi*self.radius

class Triangle(Shape):
    def init(self,base,height,a,b,c):
        self.base=base
        self.height=height
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return (1/2*self.base*self.height) 
    def perimeter(self):
        return self.a+self.b+self.c
    
if __name__ == "__main__":
 x=Circle(10)
 print(x.area())
 print(x.perimeter())

 y=Triangle(4,10,2,4,6)
 print(y.area())
 print(y.perimeter())
 