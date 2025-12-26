import pandas as pd

'''
the below method is not efficient
as the data selection is called as 
sampling bias specially selection bias
'''
print("manual selection")
print()
data = {
         "stud_id":[1,2,3,4,5,6,7,8,9,10],
         "study_hours":[2,3,4,5,6,2,1,7,8,9]
        } # assume this as a entire population

df0 = pd.DataFrame(data)
print(df0.head(5)) # sample data but with bias
print()

'''
the correct way to select is as below 
with random sampling 
'''
print("ramdon selection with random_state")
df1 = df0.sample(n=5,random_state = 42) # selects ones randomly but stable
print(df1)
print()

print("random selection without random_state")
df2 = df0.sample(n=5) # always returns ramdon data
print(df2)


''' mean difference in both population mean and sample mean'''

print("population mean :",df0["study_hours"].mean())
print("sample mean: ",df2["study_hours"].mean())

'''
          interpretation
it fixes human picking manually with bias
convenience selection

it not fixes missing data dropout in data etc miss biases
'''
