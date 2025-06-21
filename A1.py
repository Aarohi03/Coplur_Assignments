#1) Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.
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



#2) Input 2 strings concatenate them and store in another variable. then perform generally used string methods on it
str1= input("Enter string 1 : ")
str2= input("Enter string 2 : ")
a= str1 + str2
print (a)
print("Uppercase:", a.upper())
print("Lowercase:", a.lower())
print("Title Case:", a.title())
print("Count of 'o':", a.count('o'))
print("Length:", len(a))
print("Replace 'o' with '*':", a.replace('o', '*'))
print("Starts with 'I'? :", a.startswith("I"))
print("Ends with 'p'? :", a.endswith("p"))
print(a.center(50))
b="lvyhnad"
c="2468013"
encoding=str.maketrans(b,c)
print("Encoding : ", a.translate(encoding))