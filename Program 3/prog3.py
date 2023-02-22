## prog3.py
## Sampson Ezieme
## October 30, 2016
##
## Homework 3-Loopapalooza

# Problem 1

def sumOfOdds(inclusive):
    """This function takes a number and calculates the sum,
    from adding all of the odd number between 1 and the given number."""

    counter = 0
    number = 0
    while counter <= inclusive:
        if counter % 2 == 1:
            number= counter + number
        counter = counter + 1
    return number

print(sumOfOdds(100))
       
# Problem 2

def productOfPowersOf2(exp1, exp2):
    """This function takes two numbers and calculates the product,
    from multiplying all of the powers of 2 from the first given number to the last."""

    counter = 0
    number = 1
    while counter <= exp2:
        if exp1 <= counter:
            number = (2**counter) * number
        counter = counter + 1
    return number

print(productOfPowersOf2(1, 4))

# Problem 3

def printAsterisks(number):
    """This function takes a number and prints that many Asterisks in a row."""
    
    counter = 0
    asterisks = "*"
    result = ""
    while counter < number:
        counter = counter + 1
        result = result + asterisks
    print(result)

printAsterisks(15)

# Problem 4

def printTriangle(number):
    """This function takes a number and prints a right triangle,
    where the height and width of the triangle are the given number."""

    counter2 = 0
    while counter2 < number:
        counter2 = counter2 + 1
        printAsterisks(counter2)

printTriangle(7)
   
# Problem 5

def allButMax():
    """This function asks the user to input a series of numbers (one at a time),
    then the function calculates the sum of all of the numbers entered,
    except for the highest number."""
    
    Maximum = 0
    total = 0
    while True:
        number = input("Enter next number: ")
        if number == "end":
            break
        number = float(number)
        if number > Maximum:
            Maximum = number
        total = number + total
    total = total - Maximum
    print("The sum of all values except for the maximum value is: ", total)
    return total

allButMax()
          
# Problem 6

def avgSumOfSquares():
    """This function asks the user to input a series of numbers,
    those numbers are then squared and are divided by how many number were entered
    to ultimately find the average sum of squares."""
    
    counter = 0
    total = 0
    while True:
        number = input("Enter next number: ")
        if number == "end":
            if counter == 0:
                print ("No numbers were entered.")
                return None
            break
        number = float(number)
        number = number ** 2
        total = number + total
        counter = counter + 1
    total = total / counter
    print("The average of the sum of the squares is: ", total)
    return total

avgSumOfSquares()
    

    
 
 
        
        
        
    
