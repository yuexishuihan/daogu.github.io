def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs('A'))

import math 
def move(x,y,step,angle = 0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return  nx,ny
print (move(100,100,60,math.pi/6))

import math 
def  quadratic(a,b,c):
    for item in [a,b,c]:
        if not isinstance(item,(int,float)):
            raise TypeError('bad operand type')
    result = pow(b,2) - 4*a*c
    if result <0:
        print('此方程无解')
        return
    elif result > 0:
        x1 = (-b + math.sqrt(result))/(2*a)
        x2 = (-b - math.sqrt(result))/(2*a)
        return x1,x2
    else:
        return -b/(2*a)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)


def person (name,age,*,city,job):
    print(name,age,city,job)

def f1(a,b,c = 0,*args,**kw):
    print('a =',a,'b = ',b,'c = ',c,'args = ',args,'kw =',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a =',a,'b =',b,'c =')

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num ==1:
        return product
    return fact_iter(num -1,num*product)


def move (n,a = 'A',b = 'B',c = 'C'):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
print(move(3))

def trim(s):
    if not isinstance(s,(str)):
        raise TypeError('不是字符串')
    elif s[0] == '' or s[0] ==' ':
        return trim(s[1:])
    elif s[-1] == '' or s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s
s = ' niam '
print(trim(s))

def findMinAndMax(L):
    if len(L) ==0:
        return (None,None)
    min = max =L[0]
    for i in L:
        if min >= i:
            min = i
        if max <= i:
            max = i
    return (min,max)

[x*x for x in range(1,11) if x % 2 == 0]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if  isinstance(x,str)]
print (L2)

L = [x*x for x in range(10) ]
g = (x*x for x in range(10))

def fib(max):
    n,a,b, = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

def triangles():
    N = [1]
    while True:
        yield N
        N = N+[0]
        N = [N[i-1] + N[i] for i in range(len(N))] 
g = triangles
next(g)

def normalize(name):
    return name[0].upper()+name[1:].lower()

def prod(L):
    if len(L)>0:
        return reduce(lambda x,y:x*y,L)

from functools import reduce
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def fn(x,y):
        return x*10 + y
    index = s.find('.')
    print(index)
    if index != -1:
        s0 = s[:index]
        s1 = s[index:]
        return reduce