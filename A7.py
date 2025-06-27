import pandas as pd
#1)
data = {
    'info': ['Rohan123', 'Anika', 'Hello World!', 'test@example.com','9876543210', 'aarohi@gmail.com', 'abcDEF']
}
df = pd.DataFrame(data)
print(df)

email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
df['email'] = df['info'].str.match(email)

mobile = r'^\d{10}$'
df['mobile'] = df['info'].str.match(mobile)

letters = r'^[A-Za-z]+$'
df['letters'] = df['info'].str.match(letters)
print("\n After validation...\n",df)

#2)
data = {'date': ['2025-03-01', '2025-12-03', '2025-06-27']}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
print("\n Date time..\n",df)

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_name'] = df['date'].dt.day_name()

print("\n More Info...\n",df)

#3)
print("\nCSV file....\n")
df=pd.read_csv('products-100.csv')
print(df)
print(df.to_string())
print("\nUsing Head()...\n")
print(df.head())
df = df.drop_duplicates()
df = df.fillna("Not Available")
df = df.rename(columns={'Internal ID': 'Product ID'})
print("After rename...\n",df)
print("\n Info of File...")
print(df.info())
print("\n Description of File...")
print(df.describe())
print("\n Shape of File...")
print(df.shape)
print("\n Specific column of File...")
print(df['Name'])
df['Premium Product'] = df['Price'] > 500
print(df)







