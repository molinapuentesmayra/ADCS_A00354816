# Lab 2: Analisis Diseño y Construccion de Software
# Mayra Molina
# A00354816


# myPowerList class
# defines method for a given list
# methods add, remove items, sort list
# merge as suffix or prefix another list, 
# save and read from file
class myPowerList:

    def __init__(self, lst):
        self.powerList = lst

    def add_item(self, x):
        self.powerList.append(x)

    def remove_item(self, i):
        self.powerList.pop(i)
    
    def sort_list(self):
        for i in range(len(self.powerList)):
            cursor = self.powerList[i]
            pos = i
        
            while pos > 0 and self.powerList[pos - 1] > cursor:
                self.powerList[pos] = self.powerList[pos - 1]
                pos = pos - 1
            self.powerList[pos] = cursor

    def rmerge(self, lst):
        self.powerList.extend(lst)
    
    def lmerge(self, lst):
        lst.extend(self.powerList)
        self.powerList = lst

    def saveToTextFile(self, filename):
        text_file = open(filename, "w")
        for idx, val in enumerate(self.powerList):
            if idx == len(self.powerList)-1:
                text_file.write("{}".format(val))
            else:
                text_file.write("{},".format(val))
        text_file.close()
    
    def readFromTextFile(self, filename):
        text_file = open(filename, "r")
        lines = text_file.read().split(",")
        print(lines)     
        text_file.close()

def main_pwrLst():
    print("Lab 2 PowerList - Analisis, Diseño y Construccion de Software")
    print("*****************************************************\n")

    # instantiate class
    pwrLst = myPowerList([])

    while True:
        # Get user input to determine which method to run. Will only accepting 1,7 range. 
        while True:
            method = get_input_int("Choose one of the following method for powerList:\n 1 - Add item\n 2 - Delete item\n 3 - Sort items\n 4 - Merge as prefix\n 5 - Merge as suffix\n 6 - Save to file\n 7 - Read from file\n")
            if method == "exit":
                break
            elif 1 <= method <= 7:
                break
            else:
                print("That exercise is not in Lab 1...")

        # Setup program exit on "exit" input string
        if method == "exit":
            print("***********  Exiting Lab 2  ***************")
            break

        # Dictionary set up for all functions (lab exercises)
        switcher={
            1:pwrLst.add_item,
            2:pwrLst.remove_item,
            3:pwrLst.sort_list,
            4:pwrLst.lmerge,
            5:pwrLst.rmerge,
            6:pwrLst.saveToTextFile,
            7:pwrLst.readFromTextFile,
            }

        func=switcher.get(method)

        if method == 1:
            args = input("Enter item to add to list: ")
            func(args)
        elif method == 2:
            args = get_input_int("Enter idx to remove: ")
            func(args)
        elif method == 4:
            args = input("Enter list to merge as space-separated list: ")
            lst = [i for i in args.split(' ')]
            func(lst)
        elif method == 5:
            args = input("Enter list to merge as space-separated list: ")
            lst = [i for i in args.split(' ')]
            func(lst)
        elif method == 6:
            args = input("Enter filename:")
            func(args)
        elif method == 7:
            args = input("Enter filename:")
            func(args)
        else:
            func()

        print("Current state of power List: {}".format(pwrLst.powerList))
       

import csv

# Create a class to manage a directory of users containing data
# Name, Address, Phone, Email
# The class must be enable:
# 1- Creation of new record
# 2- Save all records in a file
# 3- Load records from a file
# 4- Search and get data from a given record
class user_db:
    users = dict()

    def newRecord(self):
        print("Enter name, address, phone and email separated by commas: ")
        name, address, phone, email = input().split(",")
        self.users[name] = {"Address": address, "Phone": phone, "Mail": email}
        return

    def saveToFile(self):
        with open('user_db.csv', 'w') as file:
            for user in self.users:
                file.write("{},{},{},{}\n".format(user, self.users[user]["Address"], self.users[user]["Phone"], self.users[user]["Mail"]))

    def readFromFile(self):
        with open('user_db.csv') as file:
            raw_data = csv.reader(file, delimiter=',')
            for field in raw_data:
                self.users[field[0]] = {"Address": field[1], "Phone": field[2], "Mail": field[3]}
        return

    def searchRecord(self):
        name = input('Input name (case sensitive): ')
        user = self.users.get(name)
        if user != None:
            print("User found!\nName: {},{}\n".format(name, user))
        else:
            print("User not found\n")


def main_users():
    print("Lab 2 User Records - Analisis, Diseño y Construccion de Software")
    print("*****************************************************\n")

    # instantiate class
    user_records = user_db()

    while True:
        # Get user input to determine which method to run. Will only accepting 1,7 range. 
        while True:
            method = get_input_int("Choose one of the following method for user records:\n 1 - Create new record\n 2 - Save to file\n 3 - Read from file\n 4 - Search records\n")
            if method == "exit":
                break
            elif 1 <= method <= 4:
                break
            else:
                print("That method is not included...")

        # Setup program exit on "exit" input string
        if method == "exit":
            print("***********  Exiting Lab 2  ***************")
            break

        # Dictionary set up for all functions (lab exercises)
        switcher={
            1:user_records.newRecord,
            2:user_records.saveToFile,
            3:user_records.readFromFile,
            4:user_records.searchRecord,
            }

        func=switcher.get(method)
        func()

# helper function to get user input, only integers
def get_input_int(str = "Enter a number: "):
    while True:
        try:
            num = input(str)
            num = int(num)
            if num >= 0:
                break
        except ValueError:
            if num == "exit":
                break
            else:
                print("That's not a number!")
    return num


x = get_input_int("Please select a mode:\n1 - power list\n2 - for client directory\n")
if x == 1:
    main_pwrLst()
else:
    main_users()