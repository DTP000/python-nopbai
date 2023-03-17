def fac(n) :
    if n == 0 :
        return 1
    return n * fac(n-1)
def pow(x,n):
    return x**n

def bt1(x):
    eps = 0.000000000000001
    mu = 1
    first = 1
    second = first + x**mu / fac(mu)
    while abs(first - second) > eps:
        mu -= -1
        first = second
        second = first + x**mu / fac(mu)
    return second

def bt2(x):
    first = 1
    temp = 1
    dau = -1
    eps = 0.000000000000001
    second = first + dau*(((temp+1)*(temp+2))/2)*pow(x,temp)
    while(abs(first - second) > eps ) :
        temp-=-1
        dau = - dau
        first = second
        second =  first + dau*(((temp+1)*(temp+2))/2)*pow(x,temp)
    return second

def bt3(x):
    first = x
    temp = 2
    eps = 0.000000000000001
    second = -1*first - (pow(x,temp)/temp)
    while(abs(first - second) > eps ) :
        temp-=-1
        first = second
        second = first - (pow(x,temp)/temp)
    return second

def bt4(x):
    first = 1
    mu = 1
    dau = -1
    eps = 0.000000000000001
    n = 0
    temp= (0.5)*pow(x,mu)
    second = first + (0.5)*pow(x,mu)
    while(abs(first - second) > eps ) :
        tu = 1
        mau = 4
        mu-=-1
        n=mu
        temp= (0.5)*pow(x,mu)
        first = second
        while(n>1) :
            temp =temp*(tu/mau)
            tu= tu+2
            mau=mau+2
            n -= 1
        second =  first + dau*temp
        dau = - dau
    return second

def bt5(x) :
    first = 1
    mu = 1
    dau = -1
    eps = 0.000000000000001
    n = 0
    temp = 0
    second = first - (0.5)*pow(x,mu)
    while(abs(first - second) > eps ) :
        tu = 3
        mau = 4
        mu-=-1
        n=mu
        temp= (0.5)*pow(x,mu)
        first = second
        while(n>1) :
            temp =temp*(tu/mau)
            tu= tu+2
            mau=mau+2
            n-=1
        dau = - dau
        second =  first + dau*temp
    return second
 
def bt6(x):
    eps = 0.000000000000001
    mu = 3
    dau =-1
    first = x
    second = first - pow(x, mu) / fac(mu)
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first - (dau * pow(x, mu) / fac(mu))
        dau = - dau			
    return second

def bt7(x) :
    eps = 0.000000000000001
    mu = 2
    dau =-1
    first = 1
    second = first - pow(x, mu) / fac(mu)
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first - (dau * pow(x, mu) / fac(mu))
        dau = - dau			
    return second

def bt8(x):
    eps = 0.000000000000001
    mu = 3
    tu = 3
    mau = 4
    first = 0.5
    count=0
    n = 0
    temp = 0
    second = first + 0.5*pow(x, mu)/mu
    while(abs(first - second) > eps) :
        mu+=2
        count +=1
        n=count
        temp= (0.5)*pow(x,mu)/mu
        first = second
        while(n>0) :
            temp =temp*(tu/mau)
            tu= tu+2
            mau=mau+2
            n-=1
        second = first + temp	
    return second

def bt9(x):
    eps = 0.000000000000001
    mu = 1
    dau =-1
    first = 1
    second = first - pow(x, mu+1) / fac(mu+2)
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first - (dau * pow(x, mu+1) / fac(mu+2))
        dau = - dau		
    return second        

def bt10(x):
    eps = 0.000000000000001
    mu = 3
    dau =-1
    first = 0.5
    second = first - pow(x, mu) / mu
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first - (dau * pow(x, mu) / mu)
        dau = - dau	
    return second

def bt11(x):
    eps = 0.000000000000001
    mu = 2
    dau =-1
    first = 0.5
    second = first - pow(x, mu) / mu
    while(abs(first - second) > eps) :
        mu-=-1
        first = second
        second = first - (dau * pow(x, mu) / mu)
        dau = - dau			
    return second

def bt12(x):
    eps = 0.000000000000001
    mu = 3
    first = 0.5
    second = first + pow(x, mu) / mu
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first +pow(x, mu) / mu	
    return second

def bt13(x):
    eps = 0.000000000000001
    mu = 3
    first = 0.5
    second = first + pow(x, mu) / fac(mu)
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first +pow(x, mu) / fac(mu)	
    return second

def bt14(x):
    eps = 0.000000000000001
    mu = 2
    first = 1
    second = first + pow(x, mu) / fac(mu)
    while(abs(first - second) > eps) :
        mu+=2
        first = second
        second = first +pow(x, mu) / fac(mu)	
    return second

print("bt1  x = 0.7, kq = ", bt1(0.7))
print("bt2  x = 0.7, kq = ", bt2(0.7))
print("bt3  x = 0.9, kq = ", bt3(0.9))
print("bt4  x = 0.7, kq = ", bt4(0.7))
print("bt5  x = 0.7, kq = ", bt5(0.7))
print("bt6  x = 0.9, kq = ", bt6(0.9))
print("bt7  x = 0.7, kq = ", bt7(0.7))
print("bt8  x = 0.7, kq = ", bt8(0.7))
print("bt9  x = 0.7, kq = ", bt9(0.7))
print("bt10 x = 0.7, kq = ", bt10(0.7))
print("bt11 x = 0.7, kq = ", bt11(0.7))
print("bt12 x = 0.7, kq = ", bt12(0.7))
print("bt13 x = 0.7, kq = ", bt13(0.7))
print("bt14 x = 0.7, kq = ", bt14(0.7))