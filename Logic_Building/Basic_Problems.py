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
    
print(find_lowest(13, 4))

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

print(check_arithematic(arr_len, number))
    
    
    
    
# arr = [1, 4, 7, 10]
# sample_arr = []

# for i in range(len(arr) - 1):
#     diff_value = arr[i + 1] - arr[i]
#     sample_arr.append(diff_value)
    
# print(sample_arr)