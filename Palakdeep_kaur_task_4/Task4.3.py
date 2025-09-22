import pandas as pd
import numpy as np
import random as r

num = np.arange(50,101)
df = pd.DataFrame({'Name':['Jagdish','Gursahib','Janhavi','Shreya','Purvi','Apoorva','Abhay','Samriddhi','Vidhi','Kartik']})
df['Maths'] = list(r.choices(num, k=10))
df['Science'] = list(r.choices(num, k=10))
df['English'] = list(r.choices(num, k=10))
print(df)
maths_avg = np.mean(df.iloc[:,1])
science_avg = np.mean(df.iloc[:,2])
english_avg = np.mean(df.iloc[:,3])
print('Maths average: ',maths_avg)
print('Science average: ',science_avg)
print('English average: ',english_avg)
df["Total"] = df.iloc[:, 1:].sum(axis=1)
print(df)
print("Highest marks scored: ",df.loc[df["Total"].idxmax(), "Name"])
df['Result'] = ["Pass" if x >= 150 else "Fail" for x in df["Total"]]
print(df)
df = df.sort_values('Total', ascending=False)
print(df)