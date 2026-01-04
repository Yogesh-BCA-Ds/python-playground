import pandas as pd
data = {
 "student_id":range(1,21),
 "gender":["M"]*14 + ["F"]*6,
 "study_hours":[1,5,2,4,6,2,3,7,8,9,5,4,1,2,3,6,5,2,4,8]
 }
df = pd.DataFrame(data)

# chances are high that some group may miss
# print(df.sample(n=6,random_state=1))

# now stratified method 
m = df[df["gender"] == "M"].sample(frac=0.5,random_state=1)
f = df[df["gender"] == "F"].sample(frac=0.5,random_state=1)
ss = pd.concat([m,f])
print(ss)
print(ss["gender"].value_counts())
print(df["gender"].value_counts())

'''
under represented group
minority group
high variance across samples
'''
print("mean of population:",df["study_hours"].mean())
print("mean of sample:",ss["study_hours"].mean())
