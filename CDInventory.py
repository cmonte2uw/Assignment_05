#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignment 05 - CD Inventory that allows users to load data, add data, display inventory, delete entries, and save data to txt file
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# CMontejo, 2022-Aug-01, Updated tuples to dictionaries, added functionality for deleting
# Cmontejo, 2022-Aug-04, Added functionality for saving list to txt file
# CMontejo, 2022-Aug-07, Troubleshooting and updating delete functionality, updated script description
#------------------------------------------#

# Declare variables
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # row in list
dicRow = {}  # dictionary
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
# 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

# 2. Add data to the table (2d-list) each time the user wants to add data
    if strChoice == 'a':
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':intID,'Title':strTitle,'Artist':strArtist}
        lstTbl.append(dicRow)
        
# 3. Display the current data to the user each time the user wants to display the data
    elif strChoice == 'i':
        print('ID | CD Title | Artist')
        for row in lstTbl:
            print(list(row.values()))
        print()
            
# 4. Add the functionality of loading existing data
    elif strChoice == 'l':
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID':int(lstRow[0]),'Title':lstRow[1],'Artist':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
    
# 5. Add functionality of deleting an entry
    elif strChoice == 'd':
        delID = int(input('Please enter the ID of the row you want to delete: '))
        for i in range(len(lstTbl)-1):
            if lstTbl[i]['ID']==delID:
                del lstTbl[i]
                pass
        print('Row has been cleared.\n')
        
# 6. Save the data to a text file CDInventory.txt if the user chooses so
    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            for value in row.values():
                value = str(value)
                objFile.write(value + ',')
            objFile.write('\n')
        objFile.close()
        
# 7. Exit the program if the user chooses so
    elif strChoice == 'x':
        break

# 8. Prints if the user inputs an invalid option
    else:
        print('Please choose either l, a, i, d, s or x!')

