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

Once you run the python code, The program will ask to type the file name to read like below.
-
    ![user1](https://user-images.githubusercontent.com/77169787/158926878-4d269b60-84cf-4922-b92a-84aab1b89f6c.JPG)

Please put your filename.csv(with my project, it will be data.csv) like below. 
- Then it will read the file and calculate and print the maximum weight from csv file.
    ![user4](https://user-images.githubusercontent.com/77169787/158926876-99f9d0c9-59e9-4d78-99af-c7093de2bff8.JPG)

If you miss typed or your file could not find, the program will show error line below. 
- Please check your file name and try to type the correct file name again. 
    ![user2](https://user-images.githubusercontent.com/77169787/158926869-457f7bc7-2812-4dca-87c7-610d1094de7a.JPG)

