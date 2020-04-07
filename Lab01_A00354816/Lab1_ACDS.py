
import random
# Lab 1: Analisis Diseño y Construccion de Software
# Mayra Molina
# A00354816


# Lab 1 - Exercise 1
# Ask the user for two numbers: one number to check (call it num) and one
# umber to divide by (check). 
def lab1_1():
    print("Lab 1 - Exeercise 1: If check divides evenly into num")
    print("*****************************************************\n")

    while True:
        try:
            num, check = input("Enter two numbers: ").split()
            num = int(num)
            check = int(check)
            break
        except ValueError:
            print("That's not a number!")

    if (num%check == 0):
        print("The numbers you entered {} divides evently into {}".format(num,check)) 
    else:
         print("The numbers you entered {} DOES NOT divide evently into {}".format(num,check)) 
    
    return

# Generate a random number between 1 and 9 (including 1 and 9). Ask the
# user to guess the number, then tell them whether they guessed too low, too
# high, or exactly right. 
# exit on "exit" user input
def lab1_2():
    print("Lab 1 - Exercise 2: Random number guessing game")
    print("*****************************************************\n")

    gold_num = random.randint(1,9)
    cnt = 0

    while True:
        num = get_input_int("Try guessing my random number: ")
        
        if num == "exit": 
            print("Giving up after only {} guesses? Random number was {}. Exiting game".format(cnt,gold_num))
            break

        cnt += 1
        if num == gold_num:
            print("You guessed it correctly. Random number is {}".format(gold_num))
            print("It only took you {} number of guesses! Congrats..".format(cnt))
            break
        elif num < gold_num:
            print("You guessed too low!")
        else:
            print("You guessed to high!")
    return

# Lab 1 Exercise 4
# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates
def lab1_3():
    print("Lab 1 - Exercise 3: Duplicate removal")
    print("*****************************************************\n")

    # not using helper function, as this can contain all characters
    lst = input("Input your list: ").split()

    unique_list1 = set(lst)
    print("Unique list using sets: {}".format(unique_list1))

    unique_list2 = []
    for i in lst:
        if i not in unique_list2:
            unique_list2.append(i)
        
    print("Unique list using loop: {}".format(unique_list2))
    return

# Lab 1 Exercise 5
# Write a function that receives as parameters how many Fibonnaci numbers
# to generate and then generates them
def lab1_5():
    print("Lab 1 - Exercise 5: Fibonacci sequence generator")
    print("*****************************************************\n")

    fib_seq  = []

    # get user input, how long fib sequence
    num = get_input_int("Enter how many Fibonnaci numbers to generate: ")
 
    for i in range(num):
        if  i == 0:
            fib_seq.append(0)
        elif i == 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[i-2] + fib_seq[i-1])
    
    if num > 1000:
        print("Last number of Fibonacci sequence is {}".format(fib_seq[-1])) # print last item
        opt = get_input_int("Do you want the whole sequence?\n 1. Yes\n 2. No\n")
        if opt == 1:
            print(fib_seq)    # printing will take forever on big sequences
    else:
        print(fib_seq)
    return

# Lab 1 Exercise 6
# Write a function that evaluates if a given list satisfy Fibonacci sequence
# input: list of numbers, possible fibonacci sequence
# output: true or false if sequence is fibonacci
def lab1_6():
    print("Lab 1 - Exercise 6: Fibonacci sequence check")
    print("*****************************************************\n")

    fib_seq = get_input_list("Enter sequence to validate as Fibonacci: ")

    for idx,val in enumerate(fib_seq):
        print(idx,val)
        if idx <= 1:
            if idx == 0 & val != 0 | idx == 1 & val != 1:
                print("Sequence given is NOT a Fibonacci sequence. Failed check at idx {}".format(idx))
                return False
        elif val != (fib_seq[idx-2]+ fib_seq[idx-1]):
            print("Sequence given is NOT a Fibonacci sequence. Failed check at idx {}".format(idx))
            return False

    print("Sequence given is a Fibonacci sequence")
    return True
  
# Lab 1 Exercise 7
# Write a password generator function
# input: -
# output: random generated password, from 8 to 16 character
def lab1_7():
    print("Lab 1 - Exercise 7: Random password generator")
    print("*****************************************************\n")

    pwd = ""

    # list valid characters
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

    # randomize password length from 8 to 16 characters
    for x in range(random.randint(8, 16)):
        pwd += random.choice(chars)

    print("Suggested password: {}".format(pwd))
    return

# Lab 1 Exercise 8
# Write a module containing different function that computes
# input: list of numbers (data), operation to run
# output: result of the above operations
def lab1_8():
    print("Lab 1 - Exercise 8: Module containing different function that computes the")
    print(" 1. Sample mean\n 2. Sample std deviation\n 3. Median\n 4. n-Quartil\n 5. n-Percentil")
    print("*****************************************************\n")

    user_in = get_input_list()
    user_in.sort()

    while True:
        num = get_input_int("Input function to execute: ")

        if num == "exit":
            break
           
        switcher={
            1:sample_mean,
            2:sample_std_dev,
            3:median,
            4:n_quartil,
            5:n_percentile,
            }

        
        func=switcher.get(num)

        if func is not None:
            if num == 1:
                print("Sample mean = {}".format(func(user_in)))
            elif  num == 3:
                print("Median = {}".format(func(user_in)))
            else:
                func(user_in)
        else:
            print("Invalid entry")


# function receives list of data, returns sample mean
def sample_mean(user_input):
    mean = sum(user_input)/ len(user_input)
    return mean

# function receives list of data, returns sample standard deviation
def sample_std_dev(user_input):
    avg = sample_mean(user_input)
    sum = 0

    # first sum up the square of data-average
    for i in user_input:
        sum += (i - avg)**2

    # calculate std dev as the sq root of previous sum over N number of elements
    std_dev = (sum/(len(user_input)-1))**(1/2.0)

    print("Sample standard deviation = {}".format(std_dev))
    return

# function receives list of data, returns median
def median(user_input):
    length = int(len(user_input))

    # if the list is odd number of elements, we can return the middle element
    if length%2 != 0:
        median = user_input[int(length/2)]
    # if not, we return the mean of the two elements in the middle
    else:
        median = sample_mean([user_input[int(length/2)], user_input[int(length/2)-1]])
    return median

# function receives list of data, returns n-quartil
def n_quartil(user_input):
    length = int(len(user_input))

    while True:
        n = get_input_int("Enter quartile to calculate: ")
        if 1 <= n <= 3:
            break
        else:
            print("Not a valid quartile, try 1-3")

    # 2nd quartile is the median
    if n == 2:
        q = median(user_input)
    else:
        # split up the list in two parts
        inter_q1q2 = user_input[:int(length/2)]
        inter_q2q3 = user_input[int(length/2):]

        # if there's an odd number of elements, median is included in both parts
        if length%2 != 0:
            inter_q1q2.append(inter_q2q3[0])
        # 1st or 3rd quartile is median of the arrays set up

        if n == 1:
            q = median(inter_q1q2)
        elif n == 3:
            q = median(inter_q2q3)
            
    print("Q{} of given data is = {}".format(n,q))
    return

# function receives list of data, returns n-percentil
def n_percentile(user_input):
    # get user input regarding percentil n
    while True:
        n = get_input_int("Enter percentile to calculate: ")
        if 1 <= n <= 100:
            break
        else:
            print("Not a valid quartile, try 1-100")

    # formula to find idx in list corresponding to percentile
    idx = n/100*(len(user_input))

    # if its not a floating number, percentile is the mean of the idx and upper bound
    if idx.is_integer():
        percentile =  sample_mean([user_input[int(idx-1)], user_input[int(idx)]])
    # if it's a floating number, flooring it gives us the correct idx
    else:
        percentile =  user_input[int(idx)]

    print("{}-percentile of given data is = {}".format(n, percentile))
    return

    
# Lab 1 Exercise 9 
# Write a function that converts a decimal number into a Roman format
# input : user input decimal number
# output: printed roman numeral
def lab1_9():
    print("Lab 1 - Exercise 9: function that converts a decimal to roman format")
    print("*****************************************************\n")

    # get user input, expecting a decimal number
    in_dec = get_input_int("Enter decimal number to convert: ")

    # initialize roman output and roman dictionary for numerals
    out_roman = ""
    numerals = {1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    
    # iterate in reverse order through the roman dictionary, this will be in descending order
    for val,numeral in sorted(numerals.items(), reverse=True):
        quotient = int(in_dec/val)

        # if quotient is at least 1, a new roman numeral can be added. 
        # also update decimal number for what is already converted to roman
        if quotient >= 1:
            out_roman += numeral*quotient
            in_dec    -= val*quotient

    print("Roman numeral is: {}".format(out_roman))
    return

def main():
    print("Lab 1 - Analisis, Diseño y Construccion de Software")
    print("*****************************************************\n")

    while True:
        # Get user input to determine which lab to run. Will only accepting 1,9 range. 
        while True:
            lab = get_input_int("Please enter the exercise to execute: ")
            if lab == "exit":
                break
            elif 1 <= lab <= 9:
                break
            else:
                print("That exercise is not in Lab 1...")

        # Setup program exit on "exit" input string
        if lab == "exit":
            print("***********  Exiting Lab 1  ***************")
            break

        # Dictionary set up for all functions (lab exercises)
        switcher={
            1:lab1_1,
            2:lab1_2,
            3:lab1_3,
            4:lab1_3,
            5:lab1_5,
            6:lab1_6,
            7:lab1_7,
            8:lab1_8,
            9:lab1_9,
            }

        func=switcher.get(lab)
        func()

# helper function to get user input, only integers
def get_input_int(str = "Enter a number: "):
    while True:
        try:
            num = input(str)
            num = int(num)
            if num > 0:
                break
        except ValueError:
            if num == "exit":
                break
            else:
                print("That's not a number!")
    return num

# helper function to get user input, only lists of integers
def get_input_list(str = "Enter data as space-separated list: "):
    while True:
        try:
            user_input = input(str)
            lst = [int(i) for i in user_input.split(' ')]
            break
        except ValueError:
            if user_input == "exit":
                break
            else:
                print("You entered a non-number character!")

    return lst


main()