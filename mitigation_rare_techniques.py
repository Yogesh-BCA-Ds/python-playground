import pandas as pd
data = {
"gender":["M"]*3 + ["F"],
"score":[60,70,65,90]
}
df = pd.DataFrame(data)
p_prop = {"M":0.5,"F":0.5}
s_prop = df["gender"].value_counts(normalize=True)
weights = {"M":p_prop["M"]/s_prop["M"],"F": p_prop["F"]/s_prop["F"]}


df["weight"] = df["gender"].map(weights)

print(df)
