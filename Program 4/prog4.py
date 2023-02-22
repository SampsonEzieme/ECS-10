## prog4.py
## Sampson Ezieme
## November 9, 2016
##
## Homework 3 (Loopapalooza 2)

# Problem 1

def sumOfOdds(inclusive):
    """This function takes a number (greater than or equal to 1)
    and adds the odd integers between 1 and the value of the given argument."""
    total = 0
    number = 1
    for i in range(inclusive):
        if number % 2 == 1:
            total = total + number
        number = number + 1
    return total

print(sumOfOdds(5))

# Problem 2

def countChar(character, string):
    """This function takes two arguments (1. a character, 2. a string of whatever length)
    and returns the number of times that character appears in the string."""
    total = 0
    for letter in string:
        if letter == character:
            total = total + 1
    return total

print(countChar("a", "character"))

# Problem 3

def countDiffs(string1, string2):
    """This function takes two strings of the same length and compares them
    (character by character)
    and counts how many times the strings differ in character from the same location."""
    index = 0
    total = 0
    for i in string1:
        if string1[index] != string2[index]:
            total = total + 1
        index = index + 1
    return total

print(countDiffs("sampson", "jackson"))

# Problem 4

def avgSumOfSquares(newlist):
    """This function takes a list of numbers and
    calculates the average of the sum of squares of all the values in the list. """
    index = 0
    total = 0
    if newlist == []:
        return None
    else:
        for i in newlist:
            total = total + (newlist[index] **2)
            index = index + 1
        result = total / index
        return result

print(avgSumOfSquares([1,2,3,4]))

# Problem 5

def morseCode():
    """This function will take the inputed sentence composed of the English Alphabet
    and translate that string into International Morse Code."""
    characters = [["a",".-"],["b","-..."],["c","-.-."],["d","-.."],
                  ["e","."],["f","..-."],["g","--."],["h","...."],
                  ["i",".."],["j",".---"],["k","-.-"],["l",".-.."],
                  ["m","--"],["n","-."],["o","---"],["p",".--."],
                  ["q","--.-"],["r",".-."],["s","..."],["t","-"],
                  ["u","..-"],["v","...-"],["w",".--"],["x","-..-"],
                  ["y","-.--"],["z","--.."]]

    while True:
        morseCodeSentence = ""
        sindex = 0
        statement = input("Enter sentence to be translated (*** to end): ")
        if statement == "***":
            print("Program has ended")
            break
    
        for i in statement:
            if i == " ":
                morseCodeSentence = morseCodeSentence + "   "
                continue
            index = 0
            found = False
            for f in range(len(characters)):
                letter = characters[f][0]
                
                if i == letter:
                    found = True
                    morseLetter = characters[f][1]
                    morseCodeSentence = morseCodeSentence + morseLetter + " "
                    break
            
            if found==False:
                morseCodeSentence = morseCodeSentence + "###" + " "
                if statement == "":
                    morseCodeSentence = ""
        print("Morse code: ", morseCodeSentence)
        print()
                  
morseCode()