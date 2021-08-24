
def is_prime(number):
    if number in (0, 1, 2, 4):
        return False

    for cur in range(2, number//2):
        if not number % cur:
            return False
    return True


is_prime(4)
