import math

def brute_force(f,a,b,N):
    """
    Print all the solutions of f(x)=0 in interval [a,b]

    INPUT: 
    f (function): Function for which we want to solve f(x)=0
    a,b (floats): Left and right boundaries of the interval [a,b]  
    N (int): number of cells in which [a,b] is divided.
    OUTPUT: None
    """
    dx = (b-a)/N
    for i in range(0,N):
        p = a+dx
        if f(a)*f(p)<0:
            #then there is a zero in this interval
            print(p)
        a = p

def f(x):
    y = (x-math.pi/2)*(x-math.pi)
    return y

def g(x):
    y = math.cos(x)
    return y

def h(x):
    y = x**2+1
    return y

def f2(x):
    y = x**2
    return y


a = 0
b = 5
N = 10000000
#print_all_zeros(f,a,b,N)
print_all_zeros(g,a,b,N)
#print_all_zeros(h,a,b,N)
#print_all_zeros(f2,a,b,N) #update test to <=0
