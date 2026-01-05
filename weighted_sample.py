import pandas as pd
data = {"gender":["M"]*6+["F"]*4,"study_hours":[5,4,2,6,7,8,2,3,5,4]}
df = pd.DataFrame(data)
print("="*50)
print(df["gender"].value_counts()),print(),print("="*50)
s_prop = df["gender"].value_counts(normalize=True) # it gives in fraction 
print(s_prop)
print(),print("="*50)
'''
now we will assume population how it looks here important point is 
if our population assumption is wrong then things can go wrong
thats why weighting is risky
'''
p_prop = {
"M":0.5,
"F":0.5}

'''
to calculate weights we use 
weight = population proportion/sample proportion
'''
weights = {}
for group in s_prop.index:
    weights[group] = p_prop[group]/s_prop[group]
print(weights),print("-"*50),print()
df["weight"] = df["gender"].map(weights)
print(df),print('-'*50),print()

weighted_mean = (df['study_hours']*df['weight']).sum()/df['weight'].sum()
print("weighted mean:",weighted_mean),print('-'*50),print()
