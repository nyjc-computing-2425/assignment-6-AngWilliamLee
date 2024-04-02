import datetime
import time

# Part 1
def clock(n):
    """
    Shows the time and update it once every second, for n number of seconds.

    Parameter
    ---------
    n: int
       The number of seconds to update the time for

    Returns
    -------
    string
        Current time in HH:MM:SS format which constantly updates for n seconds
    """
    timer = 0
    while timer < n:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end='\r')
        timer += 1
        time.sleep(1)


# Part 2
def lcm(a, b):
    """
    Given 2 integers, finds their lowest common multiple

    Parameter
    ---------
    a: int
    b: int

    Returns
    -------
    int
        lowest common multiple of a and b
    """
    a_original = a
    b_original = b
    while a != b:
        if a > b:
            b += b_original
        elif a < b:
            a += a_original

    return a


# Part 3
def gcf(a, b):
    """
    Given 2 integers, finds their greatest cinnib factor using euclid's algorithm

    Parameter
    ---------
    a: int
    b: int

    Returns
    -------
    int
        greatest common factor of a and b
    """
    check = False
    while not check: 
        if b == 0:
            return a
        else:
            r = a % b
            a = b
            b = r
            check = False

