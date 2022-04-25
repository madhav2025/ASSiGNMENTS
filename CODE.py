#Question 1
print("\n\n" , "-"*70, "\n" , "1".center(70," "), "\n" , "-"*70, "\n")
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number: "))
num3 = float(input("Enter the Third number: "))
average_of_numbers = (num1 + num2 + num3) / 3
print("The Average of the three numbers is : " , average_of_numbers)

print("\n\n" , "-"*70, "\n" , "2".center(70," "), "\n" , "-"*70, "\n")

#Question 2
no_of_seconds = int(input("Enter the no. of Seconds: "))
minutes = no_of_seconds // 60
seconds = no_of_seconds % 60
print("Minutes ", minutes, "and Seconds", seconds)

print("\n\n" , "-"*70, "\n" , "3".center(70," "), "\n" , "-"*70, "\n")

#Question 3
gross_income = float(input("Please enter your Gross Income : "))
no_of_dependents = int(input("Enter the no. of Dependents: "))
# Formula for Taxable Income
# Taxable income = Gross Income - Standard Deduction - (Deduction for each dependent * No. of Dependents)
taxable_income = gross_income - 10000 - (3000 * no_of_dependents)
income_tax = taxable_income * (0.2)
print("Your Income tax is: ", income_tax)

print("\n\n" , "-"*70, "\n" , "4".center(70," "), "\n" , "-"*70, "\n")


#Question 4
num1 = 25
num2 = '25'
num3 = 25.0
addition_of_numbers = num1 + int(num2) + int(num3)
addition_of_numbers = str(addition_of_numbers)
print(addition_of_numbers)
print(type(addition_of_numbers))

print("\n\n" , "-"*70, "\n" , "5".center(70," "), "\n" , "-"*70, "\n")

#Question 5
import math
angle = 0
while angle < 345:
    print(angle, round(math.sin(angle) , 4), round(math.cos(angle) , 4))
    angle += 15
