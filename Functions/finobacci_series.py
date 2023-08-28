#This functions writes a finobacci series upto n

#define finobaccci series upto n
def fib(n):
    #print series
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b =b, a+b
    
    print()
#call the function
#fib(5000)


