class Figure:
    color = "white"
    def changecolor(self,newcol):
        self.color = newcol
        
        
    def settings(self):
        print("square -",self.color,self.length,self.width)
    def settings1(self):
        print("oval -",self.color,self.radius1,self.radius2)
    
    
class Oval(Figure):
    def __init__(self,r1,r2):
        self.radius1 = r1
        self.radius2 = r2
        if r1 == r2:
            print("#ERROR not an oval")
        
class Square(Figure):
    def __init__(self,a,b):
        self.length = a
        self.width = b
        if a > b or a < b:
            print("#ERROR not a square")
                        
oval1 = Oval(5,6)
square1 = Square(6,6)
print("-_-_-_-_-_-_-_-_-_-_-_-_-")
oval1.settings1()
square1.settings()
print("-_-_-_-_-_-_-_-_-_-_-_-_-")
oval1.changecolor("green")
square1.changecolor("yellow")
oval1.settings1()
square1.settings()
