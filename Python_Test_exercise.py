

# Ex 15
# Write a Unit Test Python program to check if the sum of two numbers are equal or not!
# The Unit Test has 3 possible outcomes:
# 1. OK: if the test cases are successfully pass.
# 2. Failure: if any of test case failed and raised an exception.
# 3. Error: if any exception is raised but different from AssertionError exception.
# Hint: import calc from Ex 7, assertEqual(), import TestCase
# Test the exercise using the tool pytest.


from unittest import TestCase
import calc

class Check(TestCase):
    def test_sum(self):

        x = calc.addition(3,6)
        self.assertEqual(9,x)



# Ex 16
#Write a Unit Test Python program to check if the given word has only upper case or including any lower case.
# Hint: assertTrue(), isupper.

from unittest import TestCase
# Test the exercise using the tool pytest

class myTest(TestCase):

    def test_upper_true(self):
        self.assertTrue('MINDROAD'.isupper())



# Ex 17
# Write a Unit Test Python program to check if the longest word from a file is matched or not!
# Hint: Use Ex 12 to solve this task.
from Python_Exercise import long_short_word
from unittest import TestCase

class Evaluate(TestCase):

    def test_long_word(self):

        result = long_short_word('employee_Salary.txt')
        self.assertEqual('MindRoad', result)



#Ex 18
# Write a Unit Test Python program to check if the given full name is equal or not, as well as if the email address is correct or not for the given name.
# Unittest.mock is a library for testing in Python, which allows you to do a test of a specific function and to do that
# you need to mock that function. As your code grows eventually you'll need to start adding mocks to your test.
# Hint: import Person class from Ex 5 to solve this task, @mock.patch.object(Person, 'display_fullname')

from Python_Exercise import Person
from unittest import TestCase, mock


class Evaluate(TestCase):
    @mock.patch.object(Person, 'display_fullname')

# Used @mock.patch.object to patch the function and passed Person class
# as the first argument to the decorator
    def test_method(self,mock_last_first_name):
       mock_last_first_name.return_value = 'Tony Homsi'
       emp = Person('Tony','Homsi',27500)
       full_name = emp.display_fullname()
       email_emp = emp.email
       self.assertEqual(mock_last_first_name.return_value, full_name, "The full name is matched")
       self.assertTrue('Tony.Homsi@mindroad.se', email_emp)




