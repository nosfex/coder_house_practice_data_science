import csv
import numpy as np
import pandas as pd
import pprint

pp = pprint.PrettyPrinter()

columna_salario_bruto = 47
columna_salario_neto = 48
def clean_value(val):
  
    val = str(val).replace('.','').replace(',', '')
    if len(str(val)) == 0 or str(val) == 'nan':
        return 0
    if np.isnan(float(val)):
        return 0
    return (int(float(val)))

def parse_csv(filename, column='0'):
    csv_dataframe = pd.read_csv(filename).fillna(0).to_numpy() 

    raw_salary = np.array([clean_value(employee[columna_salario_bruto]) for employee in csv_dataframe])
    net_salary = np.array([clean_value(employee[columna_salario_neto]) for employee in csv_dataframe])
   
    pp.pprint(raw_salary)
    pp.pprint(net_salary)

    return {'bruto':raw_salary, 'neto':net_salary}
    
def employee_median_salary(salary_array):
    return np.median(salary_array)
def employee_mean_salary(salary_array):
    return np.mean(salary_array)

salaries = parse_csv('salarios_openqube_2020.02.csv')
pp.pprint("Mediana salarios netos: {0}".format(employee_median_salary(salaries['neto'])))
pp.pprint('Medio salarios netos: {0}'.format(employee_mean_salary(salaries['neto'])))