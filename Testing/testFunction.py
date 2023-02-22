def tableToFile(destName, table):
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


def saveFile(table):
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
 
def fileToTable(inFile):
    tempTable = []
    for line in inFile:
        row = line.strip()
        newlist = list(row)
        for n in range(0, len(newlist)):
            newlist[n] = int(newlist[n])
        tempTable.append(newlist)
    inFile.close()
    return tempTable

def inputFile():
    while True:
        filename = input("Enter input file name: ")
        try:
            tempInFile = open(filename, "r")
            tempInFile.close
            break
        except:
            print("No such file. Try again.")
    return tempInFile

def generations():
    while True:
        tempGen = input("How many new generations would you like to print? ")
        try:
            tempGen = int(gen)
            break
        except:
            print("Not a valid number.")
    return tempGen


def printMatrix(table, gen):
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
    
    






    
