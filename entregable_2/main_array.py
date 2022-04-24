from statistics import median
import numpy as np
import pprint 
pp = pprint.PrettyPrinter()
def median_from_int_array(max_sample=1, array_size=1, keys=['np_array', 'np_med']) :
    int_array = np.random.randint(max_sample, size=array_size)
    obj = {keys[0]:int_array, keys[1]:np.median(int_array)} 
    return obj


val = median_from_int_array(100, 100)
pp.pprint(val['np_array'])
pp.pprint('Median: '+ str(val['np_med']))