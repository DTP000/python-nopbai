from typing import List
import bai3

def readFile() -> List[bai3.Shape]:
    shapes = []
    with open('input.txt', 'r') as f:
        while True:
            s = f.readline().strip()
            if not s:
                break
            if s == '#Rect':
                rong, dai = list(map(int, f.readline().strip().split()))
                x, y = list(map(int, f.readline().strip().split()))
                shapes.append(bai3.Rect(dai, rong, x, y))
            elif s == '#Circle':
                r = int(f.readline().strip())
                x, y = list(map(int, f.readline().strip().split()))
                shapes.append(bai3.Circle(x, y, r))
            elif s == '#Triangle':
                a, b, c = list(map(int, f.readline().strip().split()))
                x, y = list(map(int, f.readline().strip().split()))
                shapes.append(bai3.Triangle(a, b, c, x, y))
    return shapes


def findMaxArea(shapes: List[bai3.Shape]) -> float:
    mA = 0.0
    for shape in shapes:
        a = shape.dien_tich()
        if a > mA:
            mA = a
    return mA

def findMaxPer(shapes: List[bai3.Shape]) -> float:
    mP = 0.0
    for shape in shapes:
        p = shape.chu_vi()
        if p > mP:
            mP = p
    return mP

def findMaxOverlap(shapes: List[bai3.Shape]) -> int:
    max_overlap_count = 0
    for i in range(len(shapes)):
        overlap_count = 0
        for j in range(len(shapes)):
            if i != j and isOverlapping(shapes[i], shapes[j]):
                overlap_count += 1
        if overlap_count > max_overlap_count:
            max_overlap_count = overlap_count
    return max_overlap_count

def isOverlapping(shape1: bai3.Shape, shape2: bai3.Shape) -> bool:
    if isinstance(shape1, bai3.Rect) and isinstance(shape2, bai3.Rect):
        x1, y1 = shape1.x, shape1.y
        x2, y2 = x1 + shape1.rong, y1 + shape1.dai
        x3, y3 = shape2.x, shape2.y
        x4, y4 = x3 + shape2.rong, y3 + shape2.dai
        if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
            return True
        else:
            return False
    elif isinstance(shape1, bai3.Circle) and isinstance(shape2, bai3.Circle):
        distance_squared = (shape1.x - shape2.x)**2 + (shape1.y - shape2.y)**2
        radius_sum_squared = (shape1.r + shape2.r)**2
        if distance_squared < radius_sum_squared:
            return True
        else:
            return False
    else:
        return False

shapes = readFile()
maxArea = findMaxArea(shapes) #sorted(shapes, key=lambda s: s.dientich(), reverse=True)[0]
maxPer = findMaxPer(shapes) #sorted(shapes, key=lambda s: s.chuvi(), reverse=True)[0]
maxOverlapCount = findMaxOverlap(shapes)
print('Hình có chu vi lớn nhất: %f' %maxPer)
print('Hình có diện tích lớn nhất: %f ' %maxArea)
print('Có %d hình nằm chồng lên nhau nhiều nhất' %maxOverlapCount)