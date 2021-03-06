import pandas

#reading csv file
df1 = pandas.read_csv("supermarkets.csv", header=None)
print(df1)

#reading xlsx file
df2 = pandas.read_excel("supermarkets.xlsx",sheet_name=0)
print(df2)

#reading txt file
df3 = pandas.read_csv("supermarkets-commas.txt",sep=",")
print(df3)

df1 = df1.drop(df1.index[0])
print(df1) #without header
print(type(df1))
