import sys

def fib(n):
    a,b,c,d=1,0,0,1
    n=n-1
    while n>0:
        if n&1:a,b=d*b+c*a,d*(b+a)+c*b
        c,d,n=c*c+d*d,d*(2*c+d),n/2
    return a+b

if __name__ == '__main__':
    print fib(long(sys.argv[1]))
