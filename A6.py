import pandas as pd

#1)Date string to time series
dates = pd.to_datetime(['2025-01-01', '2025-01-02', '2025-01-03'])
ts = pd.Series([100, 200, 150], index=dates)
print(ts)

#2)
one=pd.DataFrame(
    {'ID':[1,2,3],
    'Name':['A1','A2','A3'],
    'Subject':['s1','s2','s3']}
)
two=pd.DataFrame(
    {'ID':[1,2,3],
     'Name':['B1','B2','B3'],
     'Subject':['s3','s4','s5']}
)

print("\nInner Merge...")
r=one.merge(two,on='ID', how='inner')
print(r)

print("Left Join...")
left = pd.merge(one, two, on='ID', how='left', suffixes=('_one', '_two'))
print(left)

one=pd.DataFrame({'ID':[1,2,3],'Name':['A1','A2','A3'],'Subject':['s1','s2','s3']})
two = pd.DataFrame({'ID':[1,2,3,4],'Name':['B1','B2','B3','B4'],'Subject':['s3','s4','s5','s6']})

print("Right Join...")
right = pd.merge(one, two, on='ID', how='right', suffixes=('_one', '_two'))
print(right)
onei = one.set_index('ID')
twoi = two.set_index('ID')
print("\nIndex based join...")
index_join = onei.join(twoi, how='left', lsuffix='_one', rsuffix='_two')
print(index_join)
#COMPARISION : merge() user column ID and join() user index ID

#3
one = pd.DataFrame({
    'ID': [1, 2, 2],
    'Subject': ['s1', 's2', 's2'],
    'Marks': [90, 80, 85]
})
two = pd.DataFrame({
    'ID': [2, 2, 3],
    'Subject': ['s2', 's2', 's3'],
    'Grade': ['A', 'B', 'C']
})
multi_key = pd.merge(one, two, on=['ID', 'Subject'], how='inner')
print("\nMerge with Multiple Keys:\n", multi_key)


#3)
df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Aarohi', 'Kartik']
})
df2 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Rysa', 'Dhruv']
})
df3 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [21, 19, 20]
})
combined = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame:", combined)

merged = pd.merge(combined, df3, on='ID', how='left')
print("\nMerged with df3:", merged)

# df.join() - joins 2 dataframes based on index, types : left, right
# pd.merge() - joins 2 dataframes based on columns, types : inner,outer
