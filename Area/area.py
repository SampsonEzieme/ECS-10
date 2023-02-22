## Area.py
## October 16, 2016
## Sampson Ezieme
##
## This function will take in a value for the radius of a circle and will compute the area.


def tip(part2):
    """This program determines the tip amount from how many diners there are on the table"""
    tip_percentage = 0.18
    if part2 >= 6:
        return tip_percentage
    else:
        ask_for_tip = float(input("Enter the desired tip percentage: "))
        return (ask_for_tip /100)
    


def whatToPay():
    """This program calculates how much a costumer should pay based on the amount of diners present and the bill amount"""
    bill = float(input("Enter the amount on your bill: "))
    diners = int(input("Enter the number of diners: "))
    tip_perc = tip(diners)
    tip_to_pay = bill * tip_perc
    print("Your bill is $ ", bill)
    print("Your tip is $ ", tip_to_pay)
    total_amount = tip_to_pay + bill
    print("Your total due is $ ", total_amount)

whatToPay()
    
    
    



