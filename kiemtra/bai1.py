import random

def randRect():
    t = "#Rect\n"
    x = str(random.randint(-20, 20))
    y = str(random.randint(-20, 20))
    a = str(random.randint(0, 200))
    b = str(random.randint(0, 200))
    t += a + " " + b + "\n"
    t += x + " " + y + "\n"
    return t

def randCircle():
    t = "#Circle\n"
    r = str(random.randint(0, 200))
    x = str(random.randint(-20, 20))
    y = str(random.randint(-20, 20))
    t += r + "\n"
    t += x + " " + y + "\n"
    return t


def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

def randABC():
    while (True):
        a = (random.randint(0, 200))
        b = (random.randint(0, 200))
        c = (random.randint(0, 200))
        if is_valid_triangle(a,b,c):
            return str(a) + " " + str(b) + " " + str(c) + "\n"

def randTriangle():
    t = "#Triangle\n"
    x = str(random.randint(-20, 20))
    y = str(random.randint(-20, 20))
    t += randABC()
    t += str(x) + " " + str(y) + "\n"
    return t

def randShape():
    s = random.randint(1,3)
    if (s == 1):
        return randRect()
    elif (s==2) :
        return randCircle()
    else:
        return randTriangle()

def randInp():
    file = open('input.txt', 'w', encoding='utf-8')
    for n in range(0, 1000):
        file.writelines(randShape())
    file.close()



#bai 1
randInp()
