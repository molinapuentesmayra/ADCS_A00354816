# Lab 2: Analisis Diseño y Construccion de Software
# Mayra Molina
# A00354816
import csv



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
        return self.powerList

    def remove_item(self, i):
        self.powerList.pop(i)
        return self.powerList

    def sort_list(self):
        for i in range(len(self.powerList)):
            cursor = self.powerList[i]
            pos = i

            while pos > 0 and self.powerList[pos - 1] > cursor:
                self.powerList[pos] = self.powerList[pos - 1]
                pos = pos - 1
            self.powerList[pos] = cursor
        return self.powerList


# instantiate class
pwrLst = myPowerList([])

def main_pwrLst(method, item, lst):
    # Dictionary set up for all functions (lab exercises)
    switcher = {
        1: pwrLst.add_item,
        2: pwrLst.remove_item,
        3: pwrLst.sort_list,
    }

    func = switcher.get(method)

    if func is not None:
        if method == 1:
            return func(item)
        elif method == 2:
            return func(item)
        else:
            return func()
    else:
        raise ValueError





# Create a class to manage a directory of users containing data
# Name, Address, Phone, Email
# The class must be enable:
# 1- Creation of new record
# 2- Save all records in a file
# 3- Load records from a file
# 4- Search and get data from a given record
class user_db:
    users = dict()

    def newRecord(self, name, address, phone, email):
        self.users[name] = {"Address": address, "Phone": phone, "Mail": email}
        return self.users

    def searchRecord(self, name):
        user = self.users.get(name)
        if user != None:
            return user
        else:
            raise ValueError


user_records = user_db()
def main_users(method, name, address, user, email):
    #print("Lab 2 User Records - Analisis, Diseño y Construccion de Software")
    #print("*****************************************************\n")

    # instantiate class

    # Dictionary set up for all functions (lab exercises)
    switcher = {
        1: user_records.newRecord,
        4: user_records.searchRecord,
    }

    func = switcher.get(method)
    if method == 1:
        return func(name, address, user, email)
    elif method == 4:
        return func(name)
    else:
        raise ValueError
