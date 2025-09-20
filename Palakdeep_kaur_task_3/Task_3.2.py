import numpy as np
import random
a=np.arange(1,21)
a=random.choices(a,k=9)
a=np.array(a)
a=a.reshape(3,3)
print(a)
print(a[0])
print(a[:,1])
print(a[1,1])
print(a[0:2,0:2])
a[1,1]=99
print(a)