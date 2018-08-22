# Warm Up 1
# Write a python program to check if the number is even or odd, the program will ask the user to input a number and print out a message.
# Hint: Use input(), print(), %.

''' num = int(input("Enter a number: "))
if(num % 2) == 0:
    print("{0} is even number".format(num))
else:
    print("{0} is odd number".format(num)) '''


# Warm Up 2
# Write a Python program to check whether a string is palindrome or not. print a message for both cases.
# Hint: Use len(), def reverse(word)


'''def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x

word = input("Give me your word:\n")
x = reverse(word)

if x == word:
    print("This is a Palindrome")
else:
    print("This is NOT a Palindrome")
'''

# Warm Up 3
# Write a Python Function that add two integral numbers in a string form and then print out the result.

'''def add(num1,num2):
    print(int(num1)+int(num2))

add("5","6") '''

# Warm Up 4
# Write a Python program using dictionary to generate integral number and its square number (n, n*n) between range of numbers. and print the result.
# The program should ask the user to input the range of the numbers, e.g. range(1,11)
# Hint: dict(), range.

'''num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

d = dict()

for n in range(num1,num2+1):
    d[n] = n*n

print(d)'''

# Warm Up 5
# Write a Python Program to generate a list and a tuple with given numbers from the user, the numbers are separated by using comma and print the result for both list and tuple types.
# Sort the given numbers in ascending and descending order and print the numbers in a comma separated sequence. Make sure to remove any duplicate numbers in the
# list before sorting.
# Hint: split(), sort(), join(), revers().

'''values = input("Input the sequence of numbers: ")

my_list = values.split(',')
tuple = tuple(my_list)
print(f"list: {my_list}")
print(f"Tuple: {tuple}")

new_list = list(set(my_list))

new_list.sort()
print("Sorted list: ", new_list)
new_list.sort(reverse=True)
print("Sorted reversed list: ", new_list)'''

#

# Warm Up 6
# Write a python program to check leap year, the program will ask the user to
# input a year and check whether it's leap year or not
# Hint: and/or, !=, ==, True, def().

'''def leap_year(l_year):
    if(((l_year % 4 == 0) and (l_year % 100 !=0)) or (l_year % 400 == 0 ) == true):
        print("it is a leap year")
    else:
        print("it's not a leap year")


year = int(input("enter a year to check if it's a leap year or not: "))
leap_year(year) '''

# Ex 1
# Write a Python program that checks whether June 24th on any given year is a Wednesday.
# Create an input field that allows the user to enter the year and shows the result if it’s correct or not!
# Hint: import datetime, import calendar calender def().
'''import datetime
import calendar

def date_year(year):
    my_date = datetime.date(year, 6, 24)
    if(calendar.day_name[my_date.weekday()] == "Wednesday"):
        print("Yes that was correct, the 24th of June from the year{0} is Wednesday".format(year))
    else:
        print("No! that was not correct, please try again!")


year = int(input("Enter the year: "))
date_year(year) '''

# Improve your program by asking the user to check a range (year from the user, the year we are now) of years
# if whether June 24th on the range of years is on Wednesday.
'''import calendar

def date_year(year):
    y = year
    while y != datetime.date.today().year:
        my_date = datetime.date(y, 6, 24)
        if(calendar.day_name[my_date.weekday()] == "Wednesday"):
            print(f"The 24th of June from the year {y} is Wednesday")
            y += 1
        else:
            y += 1
            pass


year = int(input("Enter the year: "))
date_year(year)'''

# Ex 2
# Write a Python Program for a guessing Game number, in this program ask the user to enter the guessing number,
# print out a message to show if the number is too low, too high, correct number and the number of trying times to guess the correct number.
#  Show a message if the user wants to exit from the game.
# Hint: import random
'''import random

rand_num = random.randint(1, 9)
guess = 0
counter = 0

print("Welcome to play our guessing game, press exit if you want to leave the game")
while guess != rand_num and guess != "exit":
    guess = input("Enter your guess number!: \n")

    if guess == "exit":
        print(f"You exit without guessing the correct number, and you have tried {counter} times")
        break

    counter += 1

    guess = int(guess)
    if guess < rand_num:
        print("the number you guessed is too low")
    elif guess > rand_num:
        print("the number you guessed is too high")
    else:
        print(f"Congratulation!! and it took {counter} times to guess the correct number!")'''

# Ex 3
# Write a Python program that calculate the number of lower, upper care letters, space and digits.
# Create an input field that allows the user to enter a sentence and shows the number(s) of upper and lower case letter()s,
# as well as the number(s) of pressing space and the number(s) of digit(s).
# Hint: for, def, islower(), dict ={" upper": 0}

'''
def check_str(char):
    no = {"Upper_case": 0, "Lower_case": 0, "Space": 0, "Digit":0}
    for check in char:
        if check.islower():
            no["Lower_case"] += 1
        elif check.isupper():
            no["Upper_case"] += 1
        elif check.isdigit():
            no["Digit"] += 1
        else:
            no["Space"] += 1
    return no


string_sent = input("Enter any sentence: ")
no_char = check_str(string_sent)
print("The number(s) of Upper Case letters: ", no_char["Upper_case"])
print("The number(s) of Lower Case letters: ", no_char["Lower_case"])
print("The number(s) of Space: ", no_char["Space"])
print("The number(s) of Digit: ", no_char["Digit"]) '''

# Write the same program as in the Ex3 but using regular expression method!
# Hint: import re, r"[A-Z]", re.findall
'''
import re

def check_str(char):
    upper_case = r"[A-Z]"
    lower_case = r"[a-z]"
    space_case = r" "
    digit_case = r"[0-9]"

# Using findall
    num_case = r"\d+"
    num = re.findall(num_case, char)

    if not num:
        print("You haven't type any digit numbers")
    else:
        print("The extracted numbers from the string ", num)

# Using Sub, The /D character(non digit) can be replaced by an empty string!
    num = re.sub("\D", "", char)
    print(num)

# Using Filter and Lambda
    num = list(filter(lambda x: x.isdigit(), char))
    if not num:
        print("You haven't type any digit numbers")
    else:
        print("The extracted numbers from the string ", num)



    check_upper = re.findall(upper_case, char)
    print("The number of Upper Case letters: " + str(len(check_upper)))
    check_lower = re.findall(lower_case, char)
    print("The number of Upper Case letters: " + str(len(check_lower)))
    check_space = re.findall(space_case, char)
    print("The number of Space: " + str(len(check_space)))
    check_digit = re.findall(digit_case, char)
    print("The number of Digit: " + str(len(check_digit)))


check_str(input(" Enter any sentence: "))

'''

# Ex 4
#  a Python Class (Rectangle) holding data attributes (_length, _width),
# and create a  method to calculate the area of the rectangular.
# Ask the user to input the length and width of the rectangular and print the result of the area.

'''class Rectangle:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def area(self):
        return self._width*self._length


W = int(input("Enter the Width of the Rectangular: "))
L = int(input("Enter the Length of the Rectangular: "))

rectang = Rectangle(W,L)
print("Area of the Rectangular:  ",rectang.area())
'''


# Ex 5
# Create a Python Class (Person) holding data attributes (first_name, last_name, payment), the Employer class has two methods
# to display the employer full name (def display_name) and other to increase the amount of the salary (def increase_Salary), as well as including fixed rise amount of Salary
# when increasing the Salary.
# Create a class (Employer) that is inherited from the Person Class, create super method and add one extra attribute (Programming Language).
# Create another Class (Manager) that is inherited from the Person Class, this class will have extra attribute (...., emplyee = none). The Manager class has 3 methods:
# 1. To add a new employer.
# a. Print a message when you add a new employer.
# b. Print a message when the employer is already exist in the list
# 2. To remove an employer from the list.
# a. Print a message when you remove a new employer.
# b. Print a message when the employer is already remove in the list
# 3. To display all the employers name in the list.
# a. Print all the employers name in the list.
# b. Print a message if the list is empty.
class Person:
    raise_amt = 1.3

    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@mindroad.se'
        self.payment = payment

    def display_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def increase_Salary(self):
        self.payment = int(self.payment * self.raise_amt)


class Employer(Person):
    raise_amt = 1.7

    def __init__(self, first_name, last_name, payment, prog_lang):
        super(Employer, self).__init__(first_name, last_name, payment)
        self.prog_lang = prog_lang


class Manager(Person):
    def __init__(self, first_name, last_name, payment, employees=None):
        super(Manager, self).__init__(first_name, last_name, payment)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print("Added a new Employer in the System")
            print(emp.display_fullname())
        else:
            print("the name of the employer: {} It's already exist!".format(emp.display_fullname()))

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print("The Employer {} is removed from the list".format(emp.display_fullname()))
        else:
            print("the name of the employer: {} It's already deleted!".format(emp.display_fullname()))

    def display_all_emp(self):
        if self.employees == None:
            print("The List of the employers: \n")
            for emp in self.employees:
                print('==>', emp.display_fullname())
        else:
            print("The list is empty:")


emp1 = Employer('Tony', 'Homsi', 27500, 'Python')
emp2 = Employer('Adam', 'Ericsson', 25000, 'JavaScript')
print(emp1.email)
print(emp1.prog_lang)

# print(help(Employer)) # Information about what employer class inherited from the Person Class

print(emp1.payment)
emp1.increase_Salary()
print(emp1.payment)

man1 = Manager('Åsa', 'Ericsson', 60000, None)
# print(man1.email)
man1.add_emp(emp2)
man1.add_emp(emp1)

man1.remove_emp(emp1)
man1.remove_emp(emp2)
man1.display_all_emp()
# print(man1.remove_emp(emp1))
# print(man1.add_emp(emp1)) '''


# Ex 6 Write a python program using Module Method to create a simple calculator program. (add, subtract, Multiply, divide, power).
# Remember to create two files: 1. contain the all methods, e.g. Calc.py 2. contain the main program + from ....import statement.
'''from calc import addition, subtraction, division, multiplication, power


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
# Take input from the user
choice = input("Enter choice(1/2/3/4/5):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice == '1':
    print(num1, "+", num2, " = ", addition(num1, num2))

elif choice == '2':
    print(num1, "-", num2, " = ", subtraction(num1, num2))

elif choice == '3':
    print(num1, "*", num2, " = ", multiplication(num1, num2))

elif choice == '4':
    print(num1, "/", num2, " = ", division(num1, num2))

elif choice == '5':
    print(num1, "^", num2, " = ", power(num1, num2))'''


############### The Exercises (7- 9) and Warm up exercises (7 & 8) are in the Numpy_Exercise.py file ##################

# Ex 10
# Write a python program to read a specific line from a text file. The user enter the specific line,
# the program should be able to read the line either from the bottom or from the top of the page(first line or last line).
'''def read_line(f,n):
    with open(f,"r") as file:
        read_file = file.readline()
        print(list(file)[n])

n = int(input("Input the number(s) of line(s): "))
read_line('employee_Salary.txt',n)'''



# To read and find a line from a large file could take times to get the specific line.
# Read more about linecache.getline() and solve the same exercise using licecache.
'''import linecache
def read_line(f,n):
        line = linecache.getline(f,n)
        print("line %i of %s:" % (n, f))
        return line

n = int(input("Input the number(s) of line(s): "))
line = read_line("employee_Salary.txt",n)
print(line)'''

# Ex 11
# Write a Python program to read multiple line at the same time from the range selected range from the user.
# Read more about the package itertools and import islice!

'''from itertools import islice
def read_line(f,n,m):
    with open(f, "r") as file:
        line_cache = islice(file,n,m)
        print(f"The range of lines that are selected in the file {f} are between {n} and {m} \n")

        for line in line_cache:
            print(line)


n = int(input("Input the first number : "))
m = int(input("Input the second number : "))
read_line("employee_Salary.txt",n,m)
'''


# Ex 12
# Write a Python program to find the longest and shortest word in a file!
# Hint: Use import re, re.compile(), findall(), lambda(To find the longest or shortest word)


import re

def long_short_word(f):

    with open(f,"r") as file:
        words = file.read()

    pattern = "\w+"
    regex = re.compile(pattern)
    word_found = regex.findall(words)

    long_word = max(word_found, key= lambda x: len(x))
#    print(long_word)
    return long_word

    short_word = min(word_found, key= lambda x: len(x))
    return short_word
#    print(short_word)





long_short_word("employee_Salary.txt")


# Ex 13
# Write a Python program to write to an existing file!
# To write to an existing file, firstly, you need to open the file and add a parameter:
# "a" to append what you want to write to the end of the file.
# "w" to overwrite to the existing content.

'''
string = "I love MindRoad"
with open("employee_Salary.txt", "a") as write_file:
    write_file.write(string + '\n')
    write_file.close()


# Ex 14
# Write a Python program to compress and decompress a file.
# Method to compress and decompress a file using gzip module

import gzip, shutil
f_read = open("employee_Salary.txt","rb")
_compress = gzip.GzipFile("employee_Salary.txt.gz","wb")
_compress.writelines(f_read)
_compress.close()
f_read.close()


_decompress = gzip.GzipFile("employee_Salary.txt.gz", mode= 'rb')
with open("employee_Salary_decompress.txt", 'wb') as outfile:
    shutil.copyfileobj(_decompress,outfile)'''


############### The Test Exercises (15- 18) are in the Python_Test_exercise.py file ##################