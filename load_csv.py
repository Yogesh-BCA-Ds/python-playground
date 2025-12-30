import pandas as pd

df = pd.read_csv("train.csv",sep=",",encoding="latin",na_values=["NA","-","?"])
# print(df.head(2))

print()

# delimeters in csv
'''
delimiters matters some csv files have comma some different
symbols so we use sep = "," or ";" if its separated by ;
'''

# encoding in csv 
'''
its about the csv file what language its used in that same language 
pandas should read the file else error 
common languages
1. utf -8 (commonly used world wide)
2. latin-1
3. ISO-8859-1
'''
# rows and header or column name
df1 =pd.read_csv("train.csv",skiprows=1) # makes makes the 2nd row as heading
# print(df1.head(3))

df2 = pd.read_csv("train.csv",header=None)# gives default column name 
# print(df2.head()) 

print("="*25)

print('shape:',df.shape)
print('='*25)
print()
print(df.head())
print('='*25)
print()
print(df.tail())
print('='*25)
print()
print(df.isna().sum())
print("="*25)
print()
print(type(df))

df4 = pd.read_csv("train.csv")
print(df4.info(memory_usage = False))

