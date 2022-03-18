from functools import cmp_to_key
import csv

#Save the Data with the format: start, finish, value
class Data:
 
    def __init__(self, start, finish, value):
 
        self.start = start
        self.finish = finish
        self.value = value
 
#Read the CSV file and sort the list according to the 'class Data'        
def readFile():

    threeChance = 0
    fileNotOpen = True
    
    while(fileNotOpen):
        fileName=input("Please type the file name: ")
        try:
            file=open(fileName, 'r', encoding='UTF8')
        except FileNotFoundError:
            print('')
            print('----------------------------')
            print("could not open/read the file: ", fileName)
            print('----------------------------')
            print('')
        except OSError:      
            print('')
            print('----------------------------')
            print("could not open/read the file: ", fileName)
            print('----------------------------')
            print('')
        else: 
            fileNotOpen = False
        
        if threeChance == 3:
            print('')
            print('----------------------------------------------------')
            print('Could not find the file, Please check your directory.')
            print('----------------------------------------------------')
            print('')
            quit()             
        
        threeChance += 1    

    line = csv.reader(file)

    #Save CSV data line by line
    tmp = []
    for i in line:
        tmp.append(i)
    
    #Save the data in 2D list
    tmp2 = []
    for i in range(len(tmp)):
        tmp2.append([])
        for j in range(len(tmp[i])):
            tmp2[i].append(int(tmp[i][j]))
            
    #Sort the data by finishing time so that f1<=f2<=...<=fn.
    sorted(tmp2,key=lambda l:l[1])
    
    #Put sorted list into dataList    
    dataList = []
    for i in range(len(tmp2)):
        dataList.append(Data(tmp2[i][0],tmp2[i][1],tmp2[i][2]))
    
    dataLength = len(dataList)
    
    #Start find MaxVal    
    findMaxVal(dataList, dataLength)
 
# Check if there is an exist interval that does not have time conflict
def findInterval(dataList, val):
    
    #checking the inteverals from the largest finish time
    for i in reversed(range(val)):
        if dataList[i].finish <= dataList[val - 1].start:
            return i
    return -1
 
#Bottom-Up dynamic programming - unwind recursion
def findMaxVal(dataList, dataLength):
    
    #If dataLength less than 0, terminate the program
    if dataLength <0:
        print('')
        print('-----------------------------------------')
        print('Invalid Input, Please check your csv file')
        print('-----------------------------------------')
        print('')
        return 0
    
    #If datalength is 0, return dataList[0] value
    if dataLength == 0:
        return dataList[0].value
 
    #Value list saved 
    val = [None] * dataLength
    
    #input the first value(weight or profit)
    val[0] = dataList[0].value
    
    #compute p(1), p(2),....p(n)
    for i in range(1, dataLength):
 
        #dynamic program saving the cumulated value
        valCumulate = dataList[i].value
        newInterval = findInterval(dataList, i)        

        #If not overlapping interval exist, cumulate the value with current 
        if newInterval != -1:
            valCumulate += val[newInterval]
            
        #choose max value between profit current cumulated or without current
        val[i] = max(valCumulate, val[i - 1])
        
    #Data saved to the last    
    result = val[dataLength - 1]
 
    #Print the result
    print('')
    print('---------------------------------')
    print('Maximum Value Cumulated: ',result)
    print('---------------------------------')
    print('')
    
readFile()
