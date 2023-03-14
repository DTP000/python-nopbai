import math
from bai2 import Shape

class Circle(Shape):
    def __init__(self, x, y, r):
        self.r = r
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return 2*math.pi*self.r
    
    def dien_tich(self):
        return math.pi*self.r*self.r

class Rect(Shape):
    def __init__(self, dai, rong, x, y):
        self.rong = rong
        self.dai = dai
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return 2*(self.rong + self.dai)
    
    def dien_tich(self):
        return self.rong*self.dai

class Triangle(Shape):
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return self.a + self.b + self.c
    
    def dien_tich(self):
        p = self.chu_vi()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))