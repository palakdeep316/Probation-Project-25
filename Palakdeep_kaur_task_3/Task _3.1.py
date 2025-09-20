import numpy as np
import random
a=np.arange(1,101)
a=random.choices(a,k=10)
a=np.array(a)
print (np.max(a))
print (np.min(a))
print (np.average(a))
print (np.sum(a))
print (np.argmax(a))
print (np.argmin(a))
print (np.sort(a))