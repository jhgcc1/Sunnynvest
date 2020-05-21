
import numpy as np


array_discounted_payback=[-10,-5,-4,-3,4]
lenght=len(array_discounted_payback)
pb=0
for index,npv in enumerate(reversed(array_discounted_payback)):
    if npv>=0 and array_discounted_payback[::-1][index+1]<0 and index!=0:
        pb=lenght-index-1
        break
print(pb)
