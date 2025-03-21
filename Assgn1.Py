import operator
operator = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
#ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
Number1 = float(input("Enter number"))
op = input("Enter an operator(+,_,*,/):")
Number2 = float(input("Enter second number"))
if op in operator:
    result = operator[op](Number1,Number2)
    print(f"{Number1} {op} {Number2} = {result}")
else:
    print("Invalid Operator!")

