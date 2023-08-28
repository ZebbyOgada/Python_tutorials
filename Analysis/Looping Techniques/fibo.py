#learning modules . A module is a file that can be used at any instance by the interpreater in a main program
#or another module. It may contain function definitions and more
#a module can be imported into ther main program using the import command
#modules are crated with .py after the file name e.g fibo.py

#as an example, consider a module fibo.py which will return the finovacci series upto n

def fib(n):     #writes finobacci series upto n
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a+b
        print()

def fib2(n):    #write finobacci series upto n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result
