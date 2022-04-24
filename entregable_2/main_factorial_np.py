
import numpy as np
import pprint
pp = pprint.PrettyPrinter()
def factorial_by_np():
   

    val_int = int(input('Ingrese factorial a calcular: '))
    pp.pprint('Factorial: {0}'.format(np.math.factorial(val_int)))

def series_sum_by_np(x, y):

   

    np_array = np.arange(y+1)
    slice_array = np_array[x:y+1]
    pp.pprint('Valores a sumar: {0}'.format(slice_array))
    sum_array = np.sum(slice_array)
    pp.pprint('Sumatoria: {0}'.format(sum_array))

#factorial_by_np()

val_start = int(input('Ingrese inicio serie: '))
val_end = int(input('Ingrese final serie: '))
assert val_end > val_start, 'El valor final de la serie tiene que ser mayor al inicial'
#pp.pprint('El valor final de la serie tiene que ser mayor al inicial')
series_sum_by_np(val_start, val_end)