# TEST DRIVEN DEVELOPMENT

# 1 -> 1 
# 2 -> 2
# 3 -> "Fizz" 
# 5 -> "Buzz"
# 15 -> "FizzBuzz"
# print upto 100

# PYTHONPATH=src pytest (put in terminal so it knows to look in src folder) or import following:
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fizzbuzz import fizzbuzz
from fizzbuzz import print_fizzbuzz


# testing that 1 returns 1 
def test_normal_num_is_num():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_multiple_of_three():
    assert fizzbuzz(3) == "Fizz"
    
def test_multiple_of_five():
    assert fizzbuzz(5) == "Buzz"

def test_multiple_of_three_and_five():
    assert fizzbuzz(15) == "FizzBuzz"

def test_print_fizzbuzz(capsys):
    print_fizzbuzz(3)
    captured_stdout = capsys.readouterr().out
    assert captured_stdout == "1\n2\nFizz\n"

def test_print_fizzbuzz(capsys):
    print_fizzbuzz(15)
    captured_stdout = capsys.readouterr().out
    assert captured_stdout == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"