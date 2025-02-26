#1
#1 Even Number
def even_num(lst):
  return [num for num in lst if num % 2 == 0]

#2 Remove duplicates and sort
def remove_duplicates_sort(words):
    return sorted(list(set(words)))

#3 Second largest number
def second_largest(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            second, first = first, num
        elif second < num < first:
            second = num
    return second 

#4 Rotate list by K positions
def rot_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

#5 Merge two sorted lists without built-in sorting
def merge_sort_lists(lst1, lst2):
    merged = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged

#2
#1 Return a tuple with only prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_tuple(tpl):
    return tuple(num for num in tpl if is_prime(num))

#2 Convert list of tuples into two separate lists
def splt_tuples(lst):
    return [x[0] for x in lst], [x[1] for x in lst]

#3 Find the most frequently occuring element in a tuple
from collections import Counter

def most_freq_element(tpl):
    return Counter(tpl).most_common(1)[0][0]

#4 Sum of squares of all elements in a tuple
def sum_squares(tpl):
    return sum(x ** 2 for x in tpl)

#5 Merge 2 tuples and return sorted tuple
def merge_sort_tuples(tpl1, tpl2):
    return tuple(sorted(tpl1 + tpl2))


#3
#1 Count frequency of characters in a string
def char_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

#2 Swap keys and values
def swap_keys_values(d):
    return {v: k for k, v in d.items()}

#3 Merge dictionary
def merge_dict(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = merged.get(k, 0) + v
    return merged

#4 Key with maximum value
def key_maxval(d):
    return max(d, key=d.get)

#5 Sort by desc order
def sort_students(students):
    return sorted(students, key=lambda x: x['marks'], reverse=True)


#4
#1 Prime num between 10 & 50 
for num in range(10, 51):
    if is_prime(num):
        print(num, end=" ")

#2 Sum of numbers divisible by 3 & 5
def sum_div_by_3_and_5(lst):
    return sum(num for num in lst if num % 3 == 0 and num % 5 == 0)

#3 Fibonacci series upto 10th
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

#4 Reverse string using loop
def rev_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

#5 Pattern
for i in range(1, 5):
    print('*' * i)


#5
#1 Age Categories
def category_age(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

#2 Largest of 3 numbers
def large_of_three(a, b, c):
    return max(a, b, c)

#3 Calculator
def calculator(a, b, op):
    return eval(f"{a} {op} {b}")

#4 Leap Year
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#5 Temperature  category
def category_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp <= 20:
        return "Cold"
    elif temp <= 35:
        return "Warm"
    else:
        return "Hot"


#6
#1 Create DataFrame from dictionary
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

#2 Load CSV and calculate average of a column
import pandas as pd
df = pd.read_csv('test.csv')
average = df['col_name'].mean()

#3 Add new column
import pandas as pd
df['salary_after_tax'] = df['salary'] * 0.8

#4 Filter rows
import pandas as pd
filtered_df = df[df['age'] > 30]

#5 Handle missing values
import pandas as pd
df.fillna(df.mean(), inplace=True)


#7
#1 Class - Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

#2 Class - Bank Account
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        return self.balance

#3 Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

#4 Class - Car
class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage}")

#5 Inheritance
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks


#8
#1 Zero Division
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

#2 
while True:
    try:
        num = int(input("Enter an number: "))
        break
    except ValueError:
        print("Invalid input. Try again.")

#3 File Handling
try:
    with open('Test.txt') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")

#4 IndexError
def get_elem(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

#5 ValueError
def check_positive(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    return n