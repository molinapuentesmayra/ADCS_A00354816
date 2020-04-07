# Lab 1 Exercise 8
# Write a module containing different function that computes
# input: list of numbers (data), operation to run
# output: result of the above operations
def lab1_8(func_num, user_in, n):
    #print("Lab 1 - Exercise 8: Module containing different function that computes the")
    #print(" 1. Sample mean\n 2. Sample std deviation\n 3. Median\n 4. n-Quartil\n 5. n-Percentil")
    #print("*****************************************************\n")

    user_in.sort()

    switcher = {
        1: sample_mean,
        2: sample_std_dev,
        3: median,
        4: n_quartil,
        5: n_percentile,
    }

    func = switcher.get(func_num)

    if func is not None:
        if func_num == 4:
            #print("Sample mean = {}".format(func(user_in,n)))
            return func(user_in,n)
        elif func_num == 5:
            #print("Median = {}".format(func(user_in,ok on)))
            return func(user_in, n)
        else:
            return func(user_in)

    else:
        raise ValueError


# function receives list of data, returns sample mean
def sample_mean(user_input):
    mean = sum(user_input) / len(user_input)
    return mean


# function receives list of data, returns sample standard deviation
def sample_std_dev(user_input):
    avg = sample_mean(user_input)
    sum = 0

    # first sum up the square of data-average
    for i in user_input:
        sum += (i - avg) ** 2

    # calculate std dev as the sq root of previous sum over N number of elements
    std_dev = (sum / (len(user_input) - 1)) ** (1 / 2.0)

    #print("Sample standard deviation = {}".format(std_dev))
    return std_dev


# function receives list of data, returns median
def median(user_input):
    length = int(len(user_input))

    # if the list is odd number of elements, we can return the middle element
    if length % 2 != 0:
        median = user_input[int(length / 2)]
    # if not, we return the mean of the two elements in the middle
    else:
        median = sample_mean([user_input[int(length / 2)], user_input[int(length / 2) - 1]])
    return median


# function receives list of data, returns n-quartil
def n_quartil(user_input, n):
    length = int(len(user_input))

    if not(1 <= n <= 3):
        raise ValueError

    # 2nd quartile is the median
    if n == 2:
        q = median(user_input)
    else:
        # split up the list in two parts
        inter_q1q2 = user_input[:int(length / 2)]
        inter_q2q3 = user_input[int(length / 2):]

        # if there's an odd number of elements, median is included in both parts
        if length % 2 != 0:
            inter_q1q2.append(inter_q2q3[0])
        # 1st or 3rd quartile is median of the arrays set up

        if n == 1:
            q = median(inter_q1q2)
        elif n == 3:
            q = median(inter_q2q3)

    #print("Q{} of given data is = {}".format(n, q))
    return q


# function receives list of data, returns n-percentil
def n_percentile(user_input, n):
    # get user input regarding percentil n

    if not(1 <= n <= 100):
        raise ValueError

    # formula to find idx in list corresponding to percentile
    idx = n / 100 * (len(user_input))

    # if its not a floating number, percentile is the mean of the idx and upper bound
    if idx.is_integer():
        percentile = sample_mean([user_input[int(idx - 1)], user_input[int(idx)]])
    # if it's a floating number, flooring it gives us the correct idx
    else:
        percentile = user_input[int(idx)]

    #print("{}-percentile of given data is = {}".format(n, percentile))
    return percentile


# Lab 1 Exercise 9
# Write a function that converts a decimal number into a Roman format
# input : user input decimal number
# output: printed roman numeral
def lab1_9(in_dec):
    #print("Lab 1 - Exercise 9: function that converts a decimal to roman format")
    #print("*****************************************************\n")

    # initialize roman output and roman dictionary for numerals
    out_roman = ""
    numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
                900: "CM", 1000: "M"}

    # iterate in reverse order through the roman dictionary, this will be in descending order
    for val, numeral in sorted(numerals.items(), reverse=True):
        quotient = int(in_dec / val)

        # if quotient is at least 1, a new roman numeral can be added.
        # also update decimal number for what is already converted to roman
        if quotient >= 1:
            out_roman += numeral * quotient
            in_dec -= val * quotient

    #print("Roman numeral is: {}".format(out_roman))
    return out_roman
