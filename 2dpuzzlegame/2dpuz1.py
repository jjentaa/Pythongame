import random

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def isinside(self,q):
        if q.x1 < self.x and self.x < q.x2 and q.y1 < self.y and self.y < q.y2:
            print("Keng jing jing")
        else:
            print("55555 pid")

class Qua:
    def __init__(self,size,guess):
        self.x1 = random.randint(1,size-1)
        self.x2 = random.randint(self.x1+1,size)
        self.y1 = random.randint(1,size-1)
        self.y2 = random.randint(self.y1+1,size)
        self.side1 = self.x2 - self.x1
        self.side2 = self.y2 - self.y1
        self.area  = self.side1*self.side2
        self.guess = guess
        print(self.side1*self.side2)

    def isarea(self):
        if self.guess == self.area:
            print("Keng jing jing")
        else:
            print("55555 pid")
        print("The area is",self.area)

p = Point(int(input("sai x ma :")),int(input("sai y ma :")))
q = Qua(21,int(input("sai area ma :")))
p.isinside(q)
q.isarea()