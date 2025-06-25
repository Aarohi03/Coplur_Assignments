import pandas as pd

#1)Panda Series
#using dictionary
Score={1:'450',2:'378', 3:'400', 4:'490'}
s=pd.Series(Score)
print(s)
#using lists
fruits=['Apple','Mango','Grapes']
f=pd.Series(fruits)
print(f)
#accessing elements
print(s[3])
print(f[0])

#2)DataFrames
#from 2D list
df=pd.DataFrame([['AAA',12,'maths'],['BBB', 15, 'eng'],['CCC', 13, 'science'],],columns=['Name','Age','Subject'])
print(df)
#from dictionary
df=pd.DataFrame({'ID':[1,2,3], 'Girls':['Aarohi','Rysa','Shivani'], 'Boys':['Harshit','Kartik','Niel']})
print(df)
#list of lists
df=pd.DataFrame([['AAA',12,'maths'],['BBB', 15, 'eng'],['CCC', 13, 'science'],],columns=['Name','Age','Subject'])
print(df)
#list of tuples
df = pd.DataFrame([('AAA', 12, 'maths'),('BBB', 15, 'eng'),('CCC', 13, 'science')], columns=['Name', 'Age', 'Subject'])
print(df)
#list of dictionary
df = pd.DataFrame({'Name': ['AAA', 'BBB', 'CCC'],'Age': [12, 15, 13],'Subject': ['maths', 'eng', 'science']})
print(df)

#3)Data Iteration
df = pd.DataFrame({'Name': ['Aarohi', 'Harshit','Kartik','Rysa'], 'Age': [21, 20,15,18]})
for index, row in df.iterrows():
    print(row['Name'], row['Age'])
print("")
for row in df.itertuples():
    print(row.Name, row.Age)
#condition
print("\n Above age 18 : ")
r= df[df['Age'] > 18]
print(r)
#iloc[]
print("\n Using iloc[] : ")
print(df.iloc[1])
#limited rows selection
print(df.loc[2:3, 'Name'])
#drop on basis of condition
print("\n Deleting row with age 18...")
df = df[df['Age'] != 18]
print(df)
#inserting a row
print("\n Inserting a row...")
df.loc[4] = ['Anika', 27]
print(df)
#create list
print("\n Dataframe to list...")
r= df.values.tolist()
print(r)




