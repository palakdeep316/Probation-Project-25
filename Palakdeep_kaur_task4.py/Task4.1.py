import pandas as pd
import random
import numpy as np
a=np.arange(1,101)
a=pd.Series(random.choices(a,k=10))
print(a)
print(a[:5])
print(a[5:])
print(max(a)," ",min(a))
print(np.mean(a))
print(list(a))