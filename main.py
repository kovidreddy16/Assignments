#Q1 - Basic List Operation
basic_list = [10, 20, 30, 40, 50]
basic_list[2] = 100
print(basic_list)


#Q2 - List Slicing
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num[:5])
print(num[-3:])


#Q3 - List Comprehension
lsquare = [x**2 for x in range(1, 11)]
print(lsquare)


#Q4 - Tuple Immutability
t = (1, 2, 3, 4)
try:
 t[1] = 10
except TypeError as e:
 print(f"Error: {e}")


#Error: 'tuple' object does not support item assignment
# We cannot change their elements after creation.


#Q5 - Tuple Unpacking
coord = (4, 5)
x, y = coord
print(f"x: {x}, y: {y}")


#Q6 - Dictionary
student = {
"name": "Alice",
"age": 21,
"grade": "A"
}


student["age"] = 22


student["subject"] = "Math"


print(student)


#Q7 - Dictionary Iteration
scores = {"Alice": 85, "Bob": 90, "Charlie": 78}


for name, score in scores.items():
 print(f"{name}: {score}")


#Q8 - Dictionary KeySearch
dict = {"Alice": 90, "John": 85, "Mark": 92}


if "Bob" in dict:
 print("Key 'Bob' exists.")
else:
 print("Key 'Bob' does not exist.")


#Q9 - For Loop - sum
num = [5, 10, 15, 20, 25]


total = 0


for n in num:
 total += n


print(f"Sum of list: {total}")


#Q10 - While Loop - Reverse Counting
count = 10


while count >= 1:
 print(count)
 count -= 1


#Q11 - Loop - Break & continue
for i in range(1, 11):
 if i == 5:
  continue
 if i == 8:
  break
print(i)


#Q12 - If - Else
num = int(input("Enter a num: "))


if num % 2 == 0:
 print("Even Num")
else:
 print("Odd Num")


#Q13 - Nested If
num = int(input("Enter a num: "))


if num > 0:
 print("Positive")
elif num < 0:
 print("Negative")
else:
 print("Zero")


#Q14 - Function with Arguments
def multiply(x, y):
 return x * y


result = multiply(5, 3)


print(f"Product: {result}")


#Q15 - Function with default parameter
def greet(name="Guest"):
 print(f"Hello, {name}!")


greet()


greet("Alice")

