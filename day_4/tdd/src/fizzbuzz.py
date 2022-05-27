#Fizzbuzz

#Write a function called fizzbuzz
#It should take in a number

#if the number is divisible by 3, return "Fizz"
#if the number is divisible by 5, return "Buzz"
#if the number is divisible by 3 AND 5, return "FizzBuzz"
#if the number is neither divisible by 3 OR 5, return number as string


def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return str(number)
