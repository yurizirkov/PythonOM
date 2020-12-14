# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")

    elif number % 3 == 0:
        print("fizz")

    elif number % 5 == 0:
        print("buzz")

    else:
        print(number)
