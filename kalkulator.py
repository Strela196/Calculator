import sys 
def calculator():
    #a var that will tell the result of whatever the user wants
    result = 0
    
    #we get the user to type what he wants
    print("""Hi! 
Please enter what you want!
after every set of numbers or an operator please use a space and please dont type letters of the alphabet! 
when you have typed everything please press enter!
Thank you""")
    #with sys we get the input from the user and store it in a 
    a = sys.stdin.readline()
    #we strip the inpunt incase it has \n
    a.strip()
    #we make a new list so that we can store information from a.split
    b = []
    b = a.split()
    #we make two new lists so that we can than sort nums and operators
    nums = []
    operators = []
    #with this for loop we sort nums and operators 
    for i in b:
        # checks if i lenght doesnt equal to 2 so that we can than know if the user want to use to the power of operation
        if len(i) != 2:
            #check if i is an operator  
            if i in "-+/*":
                operators.append(i)
            else:
                nums.append(int(i))
        else:
            #check if i is an operator
            if i in "**":
                operators.append(i)
            else:
                nums.append(int(i))
    #for loop just to get started with the operation as we require 2 numbers to start anything
    for i in nums:
        l = nums[0]
        k = nums[1]
        op = operators[0]
        if op == "+":
            result = int(l) + int(k)
        elif op == "-":
            result = int(l) - int(k) 
        elif op == "/":
            result = int(l) / int(k)
        elif op == "*":
            result = int(l) * int(k)
        else:
            result = int(l) ** int(k)
        nums.pop(0)
        nums.pop(0)
        operators.pop(0)
        break
    #if there are more nums than that nums 
    if len(nums) >=  1:
        for i in nums:
            ope = operators[0]
            if ope == "+":
                result = result + int(i)
            elif ope == "-":
                result = result - int(i) 
            elif ope == "/":
                result = result / int(i)
            elif ope == "*":
                result = result * int(i)

            operators.pop(0)
    return result
p = calculator()
print(f"here is your result {p}")
    