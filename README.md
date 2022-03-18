# Dynamic-Programming_interval_With_weight
Dynamic Programming that finds the maximum weight with no overlapping interval

## Description


This program will be reading a 'data.csv' file that will contain a list of start, finish and the value(weight or profit). The information received from the files will be in this format: 
3,5,8 

The program will take the data from a .txt file and save the information with Data class:
- start 
- finish 
- value 

After the program will sort the saved data list by increasing order of their finish time.

Once list is sorted, the Program will use the Bottom-up dynamic programming(unwind recursion) method to find the maximum cumulated value that does not makes overlap time intervals. 


## Requirements
The code was written and tested on python version 3.8.8. Therefore, equal or higher version of python is mandatory to operate the program.

If you are running in Ubuntu, and did not installed the python yet, then please follow the steps below.

- Type the code below into Ubuntu and download the python or python3.
    ![install3](https://user-images.githubusercontent.com/77169787/158924273-b3e16968-840c-403b-992e-782e0b03b700.PNG)
    ![install](https://user-images.githubusercontent.com/77169787/158924292-378a6b67-0556-44e6-a4d8-5bc5ff3da092.PNG)
    
## User Manual

Once you run the python code, The program will automatically read the data.csv file and print out the maximum cumulated value.
But before you run the python code, Please put data.csv file in your folder directory that you run the python code.

