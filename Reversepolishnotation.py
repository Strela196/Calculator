#code that solves RPN or reverse polish notation

#gathering input
import sys
print("""please enter a mathematical equation in postfix notation and separate every num or op with a space
rule: num1 num2 (any op) num3 (any op) and so on
and please dont use **""")
inpu = sys.stdin.readline()

#defining a function that calculates the solution from the given postfix input
def rpn(a):
    #new list that inherts everything from split a 
    b = a.split()
    #since we asume that the input is no complex we can define two vars that will hold items that need to be part of an operation like substraction
    num1 = None
    num2 = None
    while len(b) != 1 or str(b[0]) in "+/-*":
        if b[0] == "+":
            n = num1 + num2
            b.pop(0)
            b.insert(0, n)
        elif b[0] == "-":
            n = num1 / num2
            b.pop(0)
            b.insert(0, n)
        elif b[0] == "/":
            n = num1 - num2
            b.pop(0)
            b.insert(0, n)
        elif b[0] == "*":
            n = num1 * num2
            b.pop(0)
            b.insert(0, n)
        else:
            num1 = int(b.pop(0))
            num2 = int(b.pop(0))
    j = b[0]
    return j
result = rpn(inpu)
print(result)
#for now the time complexity is O(n^2)
