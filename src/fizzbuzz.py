# write a programme that prints the numbers from 1 to 100
# for multiples of three print "Fizz"
# for multiples of 5 print "Buzz"
# for multiples of both 3 and 5, print "FizzBuzz"

# function for fizzbuzz
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)