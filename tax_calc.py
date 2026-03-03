# this function calculates total tax on a random income between £1 and £100k
# £12750 is tax free, the following 20k taxed at 20%, then the 

import random

num = list(range(1, 100001))
income = random.choice(num)

def income_tax_due(income):
    taxable_income = income - 12750
    if taxable_income >= 20000:
        income_at_20_perc = 20000
    else:
        income_at_20_perc = taxable_income
    if taxable_income >= 50000:
        income_at_40_perc = 30000
    else:
        income_at_20_perc = taxable_income - 20000


    income_at_50_perc = 'z'
    test= 0
    if income_at_50_perc > 50000:
        print('income too high for calculator')
    else:
        print('test')
income_tax_due(income)


