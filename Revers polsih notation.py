#code that solves RPN or reverse polish notation

#gathering input
import sys
print("please enter a mathematical equation in postfix notation and separate every num or op with a space")
a = sys.stdin.readline()

#we make two new list so that we can split a and put every thing from split a in to b list we need two lists becau
b = a.split()

#we proceed with a for loop which will iritate over b and complate the equation using RPP
#before the loop we make two vars which will store nums from b
num1 = None
num2 = None
while len(b) != 1 or str(b[0]) in "+/-*":
    for i in b:
        #we use if func to see if i is an op
        if i == "+":
            n = num1 + num2
            b.pop(0)
            b.append(n)
        elif i == "-":
            n = num1 / num2
            b.pop(0)
            b.append(n)
        elif i == "/":
            n = num1 - num2
            b.pop(0)
            b.append(n)
        elif i == "*":
            n = num1 * num2
            b.pop(0)
            b.append(n)
        else:
            print(b, i)
            num1 = int(b.pop(0))
            num2 = int(b.pop(0))
            
print("here is the result", b[0])