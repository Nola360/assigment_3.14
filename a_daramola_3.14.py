#Akinola Daramola Jr
#Programming Exercise 3.14
#06/22/2022

"""
Write a program that calculates and displays a person’s body mass index (BMI).
The BMI is often used to determine whether a person is overweight or underweight for his or her height.
A person’s BMI is calculated with the following formula:



display style B M I equals w e i g h t cross times 703 divided by h e i g h t squared
where weight is measured in pounds and height is measured in inches.
The program should ask the user to enter his or her weight and height, then display the user’s BMI.
The program should also display a message indicating whether the person has optimal weight, is underweight, or is overweight.
A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25.
If the BMI is less than 18.5, the person is considered to be underweight.
If the BMI value is greater than 25, the person is considered to be overweight.
"""

#Initializing variables
BMI = 0.0
height = 0
weight = 0.0

#Declaring variables
height = float(input("What is your height? "))
weight = float(input("What is your weight? "))
BMI = weight * 703/(height * height)

#Output
print(f"Your BMI is: {BMI:.2f}")


#Conditional Statement
if BMI < 18.5:
    print(f"Underweight")
elif BMI > 25:
    print(f"Overweight")
else:
    print(f"Optimal weight")



