# The Fizz Buzz rules
# Output "FizzBuzz" if a number is divisible by both three and five
# Output "Fizz" if a number is divisible by only three
# Output "Buzz" if a number is divisible by only five
# Output the number as a string if none of the prior conditions are met
#
# Take in a number n and calculate FizzBuzz for all numbers from
# 0 to n, inclusive. Output a list of FizzBuzz results

# we break up the problem so we can apply TDD
def fizz_buzz(i: int):
    # It's a bit of overkill to do a type check for such a simple problem
    # but we are getting ready for production code, not just the interview,
    # right?
    if isinstance(i, int):
        # A key idea is that the modulo operator (%) returns the remainder
        # of the left side divided by the right. A number is divisible
        # by another number if you divide the number by the other number
        # and the remainder is zero
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return str(i)
    else:
        raise TypeError('i should be an integer')

def fizz_buzz_bulk(n: int):
    # Again, it's overkill to do this type check...
    if isinstance(n, int):
        results = []
        # Since we unit tested fizz_buzz we just need to pump the right data into it
        for i in range(n + 1):
            # append adds the item to the end of the list
            results.append(fizz_buzz(i))
        
        return results
    else:
        raise TypeError('n should be an integer')   