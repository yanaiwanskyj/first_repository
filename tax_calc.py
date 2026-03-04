# this function calculates total tax on a random income between £1 and £100k
# £12750 is tax free, the following 20k taxed at 20%, then the next amount taxed at 40%

class Taxpayer:
    def __init__(self, name, age, income):
        self.name= name
        self.__age = age ## double underscore creates priv variable
        self.income = income

    def __taxable_incomes(self):
        return self.income - 12750

    def income_tax_due(self):
        if self.__taxable_incomes() >= 20000:
            income_at_20_perc = 20000
        elif self.__taxable_incomes() > 0:
            income_at_20_perc = self.__taxable_incomes()
        else: 
            income_at_20_perc = 0
        if self.__taxable_incomes() - income_at_20_perc > 0:
            income_at_40_perc = self.__taxable_incomes() - income_at_20_perc
        else:
            income_at_40_perc = 0
        total_tax_paid = income_at_20_perc * 0.2 + income_at_40_perc*0.4
        return total_tax_paid
    
    def tax_statement(self):
        return(f"{self.name} owes {self.income_tax_due()} in tax for {self.income} earnings")
    
    def get_age(self): ### this allows you to take the private variable and call it... the underscores used earlier prevent make it private
        return self.__age
    
    def get_taxable_incomes(self):
        return self.__taxable_incomes

## declaring an object of the class - taxpayer. object named person1.
person1 = Taxpayer('Yana', 25, 50000)

print(person1.get_age()) 
print(person1.tax_statement())

print(person1.get_taxable_incomes)

print(person1)

## inheritance- create a class based on another e.g. age check


## to rename symbol across code, ctrl right click and rename




