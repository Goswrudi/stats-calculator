# doing the same thing with numpy functions 

import numpy as np 
import random


def stats_numpy():
  array = np.array([1 , 2 , 3 , 4 , 5 ]) 
  print(np.mean(array))
  print(np.median(array))

stats_numpy()


# Can we use the data as random? 

# since we do not have any user input we can definatly use the random library function...


array1 = random.randint(0 , 10)
 