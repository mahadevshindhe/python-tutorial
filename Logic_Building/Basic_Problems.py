# Q1. Check Odd/Even. Return true for even/odd for false

def odd_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# print("If number is odd/even:", odd_even(4))
# print("If number is odd/even:", odd_even(6))
# print("If number is odd/even:", odd_even(9))
# print("If number is odd/even:", odd_even(0))
# print("If number is odd/even:", odd_even(1))
# print("If number is odd/even:", odd_even(2))

# Q2. Program to print the multiplication table of a number

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
        
# multiplication_table(5)
# multiplication_table(9)
# multiplication_table(11)
# multiplication_table(13)

# Q3. Find the sum of first n natural numbers

def sum_of_natural(num):
    add = 0
    for i in range(num + 1):
       add += i
    return add

# print("Sum of nth natural number:", sum_of_natural(5))
# print("Sum of nth natural number:", sum_of_natural(7))
# print("Sum of nth natural number:", sum_of_natural(10))


# Q4. Swap the two numbers

# With using third variable 
def swap_number1(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    
    return num1, num2

# print("Swap number:\n", swap_number1(5, 10))

# Without using third variable
def swap_number2(num1, num2):
    # Tuple unpacking
    num1, num2 = num2, num1
    
    return num1, num2

# print("Swap number:\n", swap_number2(2, 4))

# Q5. Find the number closest to n and divisible by m
# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such
# number. Output the one having maximum absolute number.

def find_closest_number(n, m):
    closest = 0
    min_difference = float("inf")
    
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(i - n)
            
            if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                closest = i
                difference = min_difference
                
    return closest
    
# print("Find the closest number:", find_closest_number(13, 4))
# n = 13
# m = 4
# print(n//m)

def find_lowest(n, m):
    # finding the quotient that will be mulitple of lower or higher
    quotient = n//m
    
    lower = m * quotient
    higher = lower + m
    
    if abs(m - lower) < abs(n - higher):
        return lower
    elif abs(m - higher) > abs(n - lower):
        return higher
    else:
        # If both the distance are equal then we will return max absolute value
        return higher if abs(higher) > abs(lower) else lower
    
# print(find_lowest(13, 4))

# Q6. The dice problem
# You are given a cubic dice with 6 faces. All the indiviual faces have number printed on them the. The number are given in number in range of 1 to 6. like an odinary dice. You will be provided with faces of cube, Your task is to guess the number on opposite cube.

def dice_facing(num):
    if (num == 6 ):
        return 1
    elif (num == 1):
        return 6
    elif (num == 5):
        return 2
    elif (num == 2):
        return 5
    elif (num == 4):
        return 3
    elif (num == 3):
        return 4

# guess_number = int(input("Enter number in the range of 1 to 6:\n"))
# print(f"For the dice facing {guess_number} opposite face will have the number {dice_facing(guess_number)}")
    


# Q6. Program to check arithematic progression
def check_arithematic(arr, n):
    if (n == 1): return True
    
    diff = arr[1] - arr[0]
    
    for i in range(2, n):
        if (arr[i] - arr[i - 1] != diff):
            return False
         
    return True

arr_len = [1, 4, 7, 10]
number = len(arr_len)

# print(check_arithematic(arr_len, number))

# arr = [1, 4, 7, 10]
# sample_arr = []

# for i in range(len(arr) - 1):
#     diff_value = arr[i + 1] - arr[i]
#     sample_arr.append(diff_value)
    
# print(sample_arr)

# Q6. Write Program for sum of gemotric series 
# A gemotric series is a series with constant ration between successive terms. The first term of series is denoted by 
# a and common ration is denoted by r. The series look like this a, ar^2, ar^3, ar^4....


def gemotric_series(a, r, n):
    sum = 0
    i = 0
    
    # while i < n:
    #     sum += a
    #     a = a * r
    #     i = i + 1
    
    for _ in range(1, n+1):
        sum += a
        a = a * r
    
    return sum

# print(gemotric_series(1, 0.5, 10))
# print(gemotric_series(2, 2, 15))


# Q 7. Program to find sample interset 
# Given principle p, rate r and time t, the task is to calculate simple intereset

def simple_interest(p, r, t):
    si = (p * r * t)/100
    
    return si

# print(simple_interest(10000, 5, 5))
# print(simple_interest(3000, 7, 1))

# Program to find the area of circle
# Given the radius r. Find the area of circle. The area of circle should be correct upto 5 decimal places 

import math

def radius_circle(radius):
    rc = radius * radius * math.pi
    
    return round(rc, 5)

# print(radius_circle(5))
# print(radius_circle(2))

# Write a program to find Sum of digits of numbers

def sum_number(num):
    digits = [int(digit) for digit in str(num)]
    sum = 0
    
    for i in digits:
        sum += i
    return sum
        
number = 12345
# print(sum_number(number))
# print(sum_number(2468))

# Check for prime numbers
# You are given number n. Check wheather it is prime or not

def prime_number(num):
    if num == 0 or num == 1:
        return False 
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

    
# print(prime_number(6))
# print(prime_number(11))

# Write a program to check is power of another number
# given two number check if y is power of x or not

def check_power(x, y):
    if x == 1:
        return y == 1
    
    pow = 1
    while pow < y:
        pow = pow * x
        
    return pow == x

# print(check_power(1, 20))

# Write a program to calcualte distance between two co-ordinates


def distance_between_co(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 4)

x1, x2 = 3, 7
y1, y2 = 4, 7
# print(distance_between_co(x1, x2, y1, y2))
# print(distance_between_co(3, 4, 4, 3))

# Check wheather if triangle is valid or not
def check_traingle(side1, side2, side3):
    
    if (side1 + side1 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
        return True
    else:
        return False
    
# print(check_traingle(7, 10, 5))
# print(check_traingle(1, 10, 12))

# Write a factorial of number
def factorial_num(num):
    sum = 1
    i = 1
    while i < num + 1:
        sum = sum * i
        i = i + 1
    
    return sum

# print(factorial_num(5))
# print(factorial_num(4))

# Write a program for square root of integer
def find_sqrt(num):
    sqrt = math.sqrt(num)
    
    if sqrt % 1 != 0:
        return math.floor(sqrt)
    else:
        return sqrt
        
# print(find_sqrt(11))

# Pair cube coun
# given count all "a" and "b" that satisfy the condition a^3 + b^3 = n where (a,b) and (b,a) are consider two different pairs

def pair_cube_count(a, b, n):
    if ((pow(a, 3) + pow(b, 3)) == n) and ((pow(b, 3) + pow(a, 3)) == n):
        return True
    else:
        return False
        
# print(pair_cube_count(1, 2, 9))
# print(pair_cube_count(1, 3, 28))
# print(pair_cube_count(3, 2, 22))

def count_cube_pairs(n):
    count = 0
    limit = int(n ** (1/3)) + 1
    
    for a in range(1, limit):
        for b in range(1, limit):
            if a ** 3 + b ** 3 == n:
                count += 1
    
    return count

# print(count_cube_pairs(9))
# print(count_cube_pairs(35))

# find the greatest common factor 

def find_factor(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors  

def greatest_common_divisor(a, b):
    factor_a = find_factor(a)
    factor_b = find_factor(b)
    
    common_factor = list(set(factor_a) & set(factor_b))
    
    return max(common_factor)
    
# print(greatest_common_divisor(30, 50))

# Program to find LCM of two numbers

# with greatest common divisor
def lcm_numbers(a, b):
    lcm = (a * b)/greatest_common_divisor(a, b)
    
    return lcm

# print(lcm_numbers(16, 28))


def least_common_factor(a, b):
    multiple_a = [i * a for i in range(1, a + 10)]
    multiple_b = [i * b for i in range(1, b + 10)]
    
    # print(multiple_a)
    # print(multiple_b)
    
    common_factors = set(multiple_a) & set(multiple_b)
    # print(common_factors)
    
    return min(common_factors)

# print(least_common_factor(30, 42))

# Perfect Number
def perfect_number(n):
    proper_div = [i for i in range(1, n) if n % i == 0]
    sum = 0
    
    for i in proper_div:
        sum += i
    
    if sum != n:
        return False
    else:
        return True
    

# print(perfect_number(15))
# print(perfect_number(6))

# Program to add two fractions

def add_two_numbers(a, b, c, d):
    if b == d:
        return f"{(a + c)}/{b}"
    else:
        return f'{(a * d) + (c * b)}/{(b * d)}'
    
    
# print(add_two_numbers(1, 5, 3, 5))
# print(add_two_numbers(1, 2, 3, 7))

# Fizz Buzz given integer n, every positive integer i <= n, the task is to print
# "FizzBuzz" if i is divisible by 3 and 5
# "Fizz" if i is divisible by 3
# "Buzz" if i is divisible by 5
# "i" as string, if none of condition are true


def fizzbuzz(n):
    store_answer = []
    
    i = 1
    while(i <= n):
        if (i % 3 == 0 and i % 5 == 0):
            store_answer.append("FizzBuzz")
        elif (i % 3 == 0):
            store_answer.append("Fizz")
        elif (i % 5 == 0):
            store_answer.append("Buzz")
        else:
            store_answer.append(str(i))
        
        i = i + 1
    
    return store_answer

# print(fizzbuzz(5))
# print(fizzbuzz(10))
# print(fizzbuzz(20))

    
# Find the day of week for the given date
def find_day(given_date, given_month, given_year):
    magic_month_arr = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    days_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    century_year_value = 0
    
    if(given_year >= 1600 and given_year <= 1699):
        century_year_value += 6
    elif(given_year >= 1700 and given_year <= 1799):
        century_year_value += 4
    elif(given_year >= 1800 and given_year <= 1899):
        century_year_value += 2
    elif(given_year >= 1900 and given_year <= 1999):
        century_year_value += 0
    elif(given_year >= 2000 and given_year <= 2099):
        century_year_value += 6
        
    # print("century_year_value", century_year_value)
    
    last_two_digit = given_year % 100
    # print("last_two_digit", last_two_digit)
    last_two_digit_div = round(last_two_digit / 4)
    # print("last_two_digit_div", last_two_digit_div)

    magic_month_num = magic_month_arr[given_month - 1]
    
    # print("magic_month_num", magic_month_num)
    
    sum_of_all = last_two_digit + last_two_digit_div + magic_month_num + century_year_value + given_date
    # print("sum_of_all", sum_of_all)
    answer_by_7 = sum_of_all % 7
    # print("answer_by_7",answer_by_7)
    
    day = days_week[answer_by_7]
        
    # print("day", day)
    return day
        

# print(find_day(14, 9, 1998))
# print(find_day(12, 8, 2010))

# Count set bits in integer
# Write an efficient program to count the number of 1s in the binary represnation of integer


def bits_in_intg(num):
    count = 0
    while (num):
        count += num & 1
        num >>= 1
    return count

# print(bits_in_intg(6))

def countSetBits(num):
    binary = bin(num)[2:]
    
    count = 0
    
    for i in binary:
        if i == "1":
            count += 1
    
    return count

# print(countSetBits(13))
# print(countSetBits(6))
# print(countSetBits(1978))

    
# num = 13    
# print(int(list(bin(num)[2:])))
# num_div = 2
# binary_arr = []

# for i in range(num):
#     quotient, remainder = divmod(num, num_div)
    
#     if quotient == 0:
#         break
#     else:
#         num = quotient
#         binary_arr.append(remainder)
#         print("quo:", quotient)
#         print("rem:", remainder)
        


# print("binary arr:", binary_arr)
# print("num:", num)

# count = 0

# for i in binary_arr:
#     if i == 1:
#         count += 1

# print(count)
# quotient, remainder = divmod(a, b)
# print(quotient, remainder)
# a = quotient
# print(a)

# Nth fibonacci series

def nth_fibonacci(n):
    if n <= 1:
        return n
    
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


# print(nth_fibonacci(3))

def nth_fibonacci_until(n, memo):
    if n <= 0:
        return n
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = nth_fibonacci_until(n - 1, memo) + nth_fibonacci_until(n - 2, memo)
    
    return memo[n]


def nth_fibona(n):
    
    # Create a memoization table and initialize with -1
    memo = [-1] * (n + 1)
    
    return nth_fibonacci_until(n, memo)

# print(nth_fibona(5))

def nth_fibonacci_series(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[-1]

# print(nth_fibonacci_series(5))

def substractOne(x):
    m = 1
    
    while((m & x ) == False):
        x = x ^ m
        m = m << 1
        
    x = x ^ m
    return x


# print(substractOne(10))

