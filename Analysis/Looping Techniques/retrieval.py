#This code retrieves strings in a disctionatry using the for command

actors = {'ben': 'the slayer','jones':'curtain raiser','brian':'the brave','robin':'the pure'} #dictionary 
for b,r in actors.items(): #for statement to retrieve literals with letters b ,r or both
    print(b,r)
print('-'*40)



#retrieval trhrough a sequence at the same time using unemerate

for i,v in enumerate(['tic','tac','toe']):
    print (i, v)
print('-'*40)

#To loop over two or more sequence at the same time and pair entries using the zip() function

questions =['name','favourite color','university ']             #list of questions
answers = ['Brian Keagan','blue','University of Minnesota']     #list of answers

for q, a in zip(questions, answers) :                           #zip function to pair entries
    print('what is your {0} ?   It is {1}'.format(q, a))        #print questions and answers
print('-'*40)

#To loop over a sequence in reverse, first specify the range

for i in reversed(range(2,15,3)):                           #sequnce from 2 to 15 with intervals of 3
    print(i)
print('-'*40)

#To loop over a sequence in sorted order without altering the source

basket = ['apple','orange','apple','pear','orange','banana']

for i in sorted(set(basket)):
    print(i)

print(basket)                                               #print original list
print('-'*40)

#creating a new list : it is often tempting to change a list while looping over it, therefore it is good courtesy\
# to create a new list instead

import math
raw_data = [54.8, 47,9, 68.5, float('NaN'), 72.1, float('NaN')]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

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









