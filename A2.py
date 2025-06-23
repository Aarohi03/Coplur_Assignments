#2) In your last program where you find the total and percentage of a student's marks of 5 subject, find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'
n= input("Enter your Name : ")
c= input("Your Class : ")
print("Enter the marks out of 100 :-")
m1= int(input("Subject 1 : "))
m2= int(input("Subject 2 : "))
m3= int(input("Subject 3 : "))
m4= int(input("Subject 4 : "))
m5= int(input("Subject 5 : "))
x= (m1+m2+m3+m4+m5)
y= ((x/500)*100)
print ("Name : " , n)
print ("Class : " , c)
print (f"Percentage =  {y}")
if y >= 90:
    print("Grade : A")
elif y >= 80:
    print("Grade : B")
elif y >= 70:
    print("Grade : C")
elif y >= 60:
    print("Grade : D")
elif y >= 50:
    print("Grade : E")
else:
    print("Fail")

#3) Input a number from user and find its factorial using for loop
n= int(input("Enter no. : "))
if (n<0):
    print("Enter non-negative no.")
else:
    f: int = 1
for i in range (1,n+1):
    f=f*i
print("The factorial of", n, "is =", f)

# Create a billing program using list. Program should have options to 1. Create Bill 2. Display Item Price and total bill amount 3. Display Total 4. Exit
items = []

while True:
    print("""
1. Add Item
2. Show Bill
3. Show Total
4. Exit
""")
    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Item name: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        items.append([name, price, qty])

    elif ch == '2':
        total = 0
        for i in items:
            print(f"{i[0]} - {i[1]} x {i[2]} = {i[1]*i[2]}")
            total += i[1] * i[2]
        print("Total = ", total)

    elif ch == '3':
        print("Total = ", sum(i[1]*i[2] for i in items))

    elif ch == '4':
        break

    else:
        print("Invalid")