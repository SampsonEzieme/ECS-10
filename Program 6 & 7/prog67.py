## prog67.py
## Sampson Ezieme
## December 2, 2016
##
## Homework 6 & 7

#Problem 6

def totalValue(i, j, Table):
    """This function takes a point within the matrix and looks at the
       surrounding points and counts up the amount of live cells around it."""
    if j < (len(Table[i]) - 1):
        a = Table[i][j+1]
    else:
        a = 0

    if j > 0:
        b = Table[i][j-1]
    else:
        b = 0

    if i < (len(Table) - 1):
        c = Table[i+1][j]
    else:
        c = 0

    if i > 0:
        d = Table[i-1][j]
    else:
        d = 0

    if 0 < i <= (len(Table) - 1) and j < (len(Table[i]) - 1):
        e = Table[i-1][j+1]
    else:
        e = 0

    if 0 <= i < (len(Table) - 1) and j < (len(Table[i]) - 1):
        f = Table[i+1][j+1]
    else:
        f = 0

    if 0 < i <= (len(Table) - 1) and j > 0:
        g = Table[i-1][j-1]
    else:
        g = 0

    if 0 <= i < (len(Table) - 1) and j > 0:
        h = Table[i+1][j-1]
    else:
        h = 0

    Total = a + b + c + d + e + f + g + h
    return Total


def liveOrDie(value, i, j, Table, copyOfTable):
    """This function determines if the current cell at point [i][j]
       should live or die based upon the total number of live cells
       surrounding it."""
    if Table[i][j] == 1:
        if value < 2:
            copyOfTable[i][j] = 0
        elif value == 2 or value ==3:
            copyOfTable[i][j] = 1
        else:
            copyOfTable[i][j] = 0
    if Table[i][j] == 0:
        if value == 3:
            copyOfTable[i][j] = 1
        else:
            copyOfTable[i][j] = 0       



def nextGen(Table):
    """This function returns the next generation of live and dead cells
       based on the table entered by following the rules of
       Conway's Game Of Life."""
    import copy
    copyOfTable = copy.deepcopy(Table)
    for i in range(0, len(Table)):
        for j in range(0, len(Table[i])):
            value = totalValue(i, j, Table)
            liveOrDie(value, i, j, Table, copyOfTable)
    return copyOfTable


# Problem 7

def printMatrix(table, gen):
    """This function takes two argument
       the number of generations to print (gen) and the initial matrix (table)
       and prints out those generations."""
    import copy
    for i in range(0, (gen + 1)):
        print("Generation: ", i)
        if i == 0:
            translation(table)
            
        else:
            table = nextGen(table)
            translation(table)
    termTable = copy.deepcopy(table)
    return termTable

def generations():
    """This function ask for an amount of generations the user will like to print
       and, based on the user's input, the funtion will determine if the input
       is a valid number."""
    while True:
        tempGen = input("How many new generations would you like to print? ")
        try:
            tempGen = int(tempGen)
            break
        except:
            print("Not a valid number.")
    return tempGen

def inputFile():
    """This function ask what file the user will like to read from
       and determines if that file exist. If the file doesn't exist,
       the function will ask the user to input another file name."""
    while True:
        filename = input("Enter input file name: ")
        try:
            tempInFile = open(filename, "r")
            tempInFile.close
            break
        except:
            print("No such file. Try again.")
    return tempInFile

def fileToTable(inFile):
    """Based on the file the user chooses, the function will turn
       the contents of that file into a 2D Table or matrix."""
    H = []
    for line in inFile:
        row = line.strip()
        newlist = list(row)
        for n in range(0, len(newlist)):
            newlist[n] = int(newlist[n])
        H.append(newlist)
    inFile.close()
    return H


def saveFile(table):
    """This function asks whether the user would like to save the last generation
       into a file. If the user doesn't want to save, the function ends.
       If the user types in yes the function will ask for a file to write to.
       If that file exist it will ask the user if they want to overwrite that file.
       If that file doesn't exist it creates a new file to save to."""
    done = input("Would you like to save the latest generation? ('y' to save): ")
    if done == "y":
        while True:
            destName = input("Enter destination file name: ")
            if file_exist(destName):
                sure = input("Do you want to overwrite that file? ('y' to continue): ")
                if sure == "y":
                    tableToFile(destName, table)
                    break
                else:
                    continue
            else:
                tableToFile(destName, table)
                break
    else:
        pass


def tableToFile(destName, table):
    """This function turns a table into a file by converting it to a sting and writing
       it to a file."""
    print()
    print("Saving data to ", destName)
    outfile = open(destName, "w")
    counter = 0
    for r in table:
        counter = counter + 1
        for c in r:
            outfile.write(str(c))
        if counter < len(table): 
            outfile.write("\n")
    outfile.close()

def file_exist(f):
    """This function takes a filename in and determines if that file exist."""
    try:
        h = open(f)
        h.close()
        return True
    except:
        return False

def translation(matrix):
    """This function turns the ones and zeros in a matrix into dots and asterisk
       and prints them."""
    for i in range(0, len(matrix)):
        starOrDots = ""
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                starOrDots = starOrDots + "." + " "
            else:
                starOrDots = starOrDots + "*" + " "
        print(starOrDots)


def life():
    """This function asks the user to input a file name and from that file prints
       how many generations the user wants based on the rules of Conway's Game Of Life.
       Then the function asks if the user wants to save the final generation to a file,
       if so the function saves the file, if not the function ends."""
    inFile = inputFile()
    gen = generations()
    table = fileToTable(inFile)
    LastTable = printMatrix(table, gen)
    saveFile(LastTable)
    return print("End of program.")

life()
