'''complete the function solveMeFirst to compute the sum of two integers
function prototype:

int solveMeFirst [int a, int b]:

where.
    a is the first integer input
    b is the second integer input

Return values
    sum of the above two integers
'''

def solveMeFirst(a, b):
    return a + b

num1 = int(input("Input your first number for summation: "))
num2 = int(input("Input your second number for summation: "))
res = solveMeFirst(num1, num2)
print(f"Sum = {res}")