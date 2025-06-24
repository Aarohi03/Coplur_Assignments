import csv
import requests

#1)Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data
address =[
    ['Name','Address','Mobile','Email'],
    ['Aarohi','361, Vaishali Nagar','555222','aarohi@gmail.com'],
    ['Harshit','357, Chitrakoot', '343434', 'harshit@gmail.com'],
    ['Anant','679, Jagatpura', '232301','anant@gmail.com'],
    ['Nyra','429, C-Scheme', '888011','nyra@gmail.com']
]

with open("address.csv",'w', newline="") as file:
    writer=csv.writer(file)
    for x in address:
        writer.writerow(x)

#2)Refer to our example of weather data and get more details. Display them

def weather_details(city,apikey):
    url="https://api.openweathermap.org/data/2.5/weather?"
    final_url = f"{url}q={city}&appid={apikey}&units=metric"

    try:
        response=requests.get(final_url)
        response.raise_for_status()
        data=response.json()

        temperature= data["main"]["temp"]
        humidity= data["main"]["humidity"]
        feels_like=data["main"]["feels_like"]
        clouds=data["clouds"]["all"]
        wind=data["wind"]["speed"]
        sunrise=data["sys"]["sunrise"]
        sunset=data["sys"]["sunset"]


        print(f"Weather in {city} : ")
        print(f"Temperature : {temperature} C (feels like : {feels_like} C)")
        print(f"Humidity : {humidity}%")
        print(f"Description : {data["weather"][0]["description"].capitalize()}")
        print(f"Clouds : {clouds}")
        print(f"Wind : {wind}")
        print(f"Sunrise : {sunrise}")
        print(f"Sunset : {sunset}")


    except requests.exceptions.RequestException as e:
        print(f"error fetching data: {e}")

apikey="38d0a2695c77e85d7223229fc143435c"
city=input("Enter City Name : ")
weather_details(city,apikey)

#3)Practise DATABASE
#create database
import sqlite3
conn=sqlite3.connect("a4.db")
#create tables
conn.execute('''
Create table if not exists classA(
s_id integer primary key autoincrement,
s_name varchar(60),
email varchar(70),
mobile varchar(10)
)
''')
conn.execute('''
Create table if not exists classB(
s_id integer primary key autoincrement,
s_name varchar(60),
email varchar(70),
mobile varchar(10)
)
''')
#insert records
conn.execute('''
INSERT INTO classA(s_id,s_name,email,mobile) VALUES ("101", "AAA", "aaa@gmail.com","345678");
''')
conn.execute('''
INSERT INTO classA(s_id,s_name,email,mobile) VALUES ("102", "BBB", "bbb@gmail.com","111222");
''')
conn.execute('''
INSERT INTO classA(s_id,s_name,email,mobile) VALUES ("103", "CCC", "ccc@gmail.com","456789");
''')
conn.execute('''
INSERT INTO classB(s_id,s_name,email,mobile) VALUES ("105", "PPP", "ppp@gmail.com","345678");
''')
conn.execute('''
INSERT INTO classB(s_id,s_name,email,mobile) VALUES ("106", "QQQ", "qqq@gmail.com","345678");
''')
conn.execute('''
INSERT INTO classB(s_id,s_name,email,mobile) VALUES ("107", "RRR", "rrr@gmail.com","345678");
''')

conn.commit()
print("\nData inserted to table")
#select operation
print("\nStudent names of class A : ")
for row in conn.execute("SELECT s_name FROM classA"):
    print(row)
print("\nStudents with s_id 106 :")
for row in conn.execute("SELECT * FROM classA WHERE s_id == 106"):
    print(row)
#update
print("\nUpdating CCC's email ")
conn.execute("UPDATE classA SET email = 'ccc_updated@gmail.com' WHERE s_name = 'CCC';")
conn.commit()
print("Data updated")
#delete
print("\nDelete QQQ")
conn.execute("DELETE FROM classB WHERE s_name = 'QQQ';")
conn.commit()
print("\nData Deleted")

