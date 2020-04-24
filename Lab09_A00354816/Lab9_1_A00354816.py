import logging
import csv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='Lab9_A00354816_LOG.log',
                    filemode='w')

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s = %(message)s")
handler.setFormatter(formatter)
logging.getLogger('').addHandler(handler)

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
        logger.info("USER DB - new user record for name %s:", name)
        return

    def saveToFile(self):
        with open('user_db.csv', 'w') as file:
            for user in self.users:
                file.write("{},{},{},{}\n".format(user, self.users[user]["Address"], self.users[user]["Phone"], self.users[user]["Mail"]))
        logger.info("USER DB - save user database to file user_dv.csv")
        return
                    
    def readFromFile(self):
        with open('user_db.csv') as file:
            raw_data = csv.reader(file, delimiter=',')
            for field in raw_data:
                self.users[field[0]] = {"Address": field[1], "Phone": field[2], "Mail": field[3]}
        logger.info("USER DB - reading database from file user_dv.csv")
        return

    def searchRecord(self):
        name = input('Input name (case sensitive): ')
        user = self.users.get(name)
        if user != None:
            print("User found!\nName: {},{}\n".format(name, user))
            logger.info("USER_DB - Search record, user found")
            return
        else:
            print("User not found\n")
            logger.warning("USER_DB - Search record, user NOT found")
            return

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
                logger.debug("EXIT")
                break
            elif 1 <= method <= 4:
                logger.info("Method chosen %s", method)
                break
            else:
                print("That method is not included...")
                logger.warning("Incorrect input")

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

main_users()
