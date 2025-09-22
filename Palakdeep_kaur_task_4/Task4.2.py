import pandas as pd
import random
import numpy as np
df=pd.DataFrame({"names":["Adi","Bobby","Candy","Dior","Ena"],"Age":[20,21,19,22,20],"Marks":[85,90,75,95,88]})
print(df)
print(df.iloc[:3,:])
print(df.names)
print(df[df['Marks'] > 85])
df['Grade'] = ['A','A','C','C','B']
print(df)
df.pop('Age')
print(df)