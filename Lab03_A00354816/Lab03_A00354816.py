# Python code to demonstrate math.factorial()
import math
import filecmp


def factorial(num):
    return math.factorial(num)


def power(num, pow):
    return math.pow(num, pow)


def filecomp(file1, file2):
    return filecmp.cmp(file1, file2)


class user_db:
    users = dict()

    def newRecord(self, name, email, age, country):
        self.users[name] = {"Email": email, "Age": age, "Country": country}
        with open("db.txt", 'a+') as output:
            output.write("{},{},{},{}".format(name, email, age, country))
        return self.users

    def deleteRecord(self, name, email, age, country):
        self.users.pop(name, None)
        with open("db.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != "name,email,age,country":
                    f.write(i)
            f.truncate()

    def searchRecordName(self, search_name):
        for names in self.users.keys():
            if search_name in names:
                return True
        return False





