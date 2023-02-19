## prog2.py
## Sampson Ezieme
## October 11, 2016
##
## Homework 2 (Yay!)

## Problem 1

def inchesToMeters(x):
    """This Function converts Inches into Meters"""
    convert_into_meters = 0.0254
    Meters = x * convert_into_meters
    return Meters


    
## Problem 2

def poundsToKgs(x):
    """This Function converts Pounds into Kilograms"""
    convert_pounds_to_Kilograms = 0.453592
    Kilograms = x * convert_pounds_to_Kilograms
    return Kilograms


## Problem 3

def bmi(height_in_meters, weight_in_kilograms):
    """This Function Calculates the BMI from a person's Height(meters) and Weight(Kg)"""
    height = height_in_meters
    weight = weight_in_kilograms
    body_mass_index = weight / (height**2)
    return body_mass_index


## Problem 4

def bodyMassIndex():
    """This Function will ask a series of questions and calculate the BMI from those inputs"""
    name =(input("Please enter the subject's name: "))
    h = float(input("Please enter the subject's height in inches: "))
    w = float(input("Please enter the subject's weight in pounds: "))
    height_input = inchesToMeters(h)
    weight_input = poundsToKgs(w)
    BMI = bmi(height_input, weight_input)
    print(name, "has a body mass index of: ", BMI)
    if BMI < 18.5:
        print(name, "is underweight")
    elif BMI >= 18.5 and BMI < 25:
        print(name, "is normal weight")
    elif BMI >= 25 and BMI < 30:
        print(name, "is overweight")
    else:
        print(name, "is obese")

bodyMassIndex()






        
    
    


    


    







