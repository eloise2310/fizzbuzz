# TEST DRIVEN DEVELOPMENT

# 1 -> 1 
# 2 -> 2
# 3 -> "Fizz" 
# 5 -> "Buzz"
# 15 -> "FizzBuzz"
# print upto 100

# PYTHONPATH=src pytest (put in terminal so it knows to look in src folder)

from fizzbuzz import fizzbuzz

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

