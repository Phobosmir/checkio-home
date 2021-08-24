"""
You are given a two or more digits number N. For this mission, you should find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist, then return 0.

Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

Hints: Remember prime numbers (numbers divisible by only one) and be careful with endless loops.

Input: A number N as an integer.

Output: The number X as an integer.

Example:

checkio(20) == 45
checkio(21) == 37
checkio(17) == 0
checkio(33) == 0
1
2
3
4
How it is used: This task will teach you how to work with numbers in code. You can factorize numbers and reconstruct them into new numbers. Of course you can solve this problem with brute force, but is that the best way? Numbers are the foundation of mathematics and programming.

Precondition:
9 < N < 105.
"""

def prime_factors(number):
    def _divides_without_reminder(number, divisor):
        return not number % divisor
    i = 2
    factors = []
    while i * i <= number:
        if _divides_without_reminder(number, i):
            number //= i
            factors.append(i)
        else:
            i += 1
    if number > 1:
        factors.append(number)
    return factors

def max_factors(number):
    def _divides_without_reminder(number, divisor):
        return not number % divisor
    i = 9
    factors = []
    while number > 9 and i > 2:
        if _divides_without_reminder(number, i):
            number //= i
            factors.append(i)
        else:
            i -= 1
    if number > 1:
        factors.append(number)
    return factors

def checkio(number):
    factors = max_factors(number)
    if any(map(lambda x: x > 9, factors)):
        return 0
    res = 0
    for digit_number, value in enumerate(factors):
        res += 10**digit_number*value
    return res


# other solutions

def checkio_2(number):
    num=number
    st=''
    while num!=1:
        for x in range (9,1,-1):
            if num%x==0:
                num=num//x
                st+=str(x)
                break
        else:
            return 0
    return int(st[::-1])


def checkio_3(n, t=''):
    for i in range(9, 1, -1):
        while not n%i:
            n, t = n//i, str(i)+t
    return n==1 and int(t)


def checkio_4(number):
    factorized = ""

    """I swear I spent 8+ hours total across several weeks on this one trying
    to somehow combine digits whose sum was smaller than 10... this is too
    complex for this exercise, don't do it.

    first factorize the number from big factors to small to
    make sure we don't end up with stuff like 2*2*3, but immediately
    insert the biggest factors"""

    for i in range(9, 1, -1):
        while number % i == 0:
            factorized += str(i)
            number = number / i

    # sort it so the smallest digit is up front
    factorized = sorted(factorized)

    # if you're left with a number that contained a prime with double digits,
    # your number from number/i will be that prime number, so return 0
    if number != 1:
        return 0
    else:
        return int("".join(factorized))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(16) == 28, "16"
    assert checkio(27) == 39, "27"
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"