#2) Write a function for basic math operations like add multiply subtract divide and use this in your program, take 2 number input from user.
a= int(input("Enter 1st no. : "))
b= int(input("Enter 2nd no. : "))
op= input("choose the operation : + - * / \n")

def add(x,y):
    print("Result : ", x+y)

def diff(x,y):
    print("Result : ", x-y)

def product(x,y):
    print("Result : ", x*y)

def quotient(x,y):
    if y!=0:
      print("Result : ", x/y)
    else:
        print(f"invalid value of 2nd no.")

if op == '+':
    add(a,b)
elif op == '-':
    diff(a,b)
elif op == '*':
    product(a,b)
elif op == '/':
    quotient(a,b)
else:
    print("invalid operator")

#3) Write a program to check Palindrome Number
p = int(input("Enter number to check palindrome : "))
n = p
rev = 0

while p > 0:
    i = p % 10
    rev = rev * 10 + i
    p = p // 10

if rev == n:
    print("Number is palindrome")
else:
    print("Number is NOT palindrome")
