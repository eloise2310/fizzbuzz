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
    
def print_fizzbuzz(highest_number):
    fizzbuzz_numbers = (fizzbuzz(i) for i in range(1, highest_number +1))
    for n in fizzbuzz_numbers:
        print(n)

if __name__ == "__main__":
    print_fizzbuzz(100)