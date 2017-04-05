# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""
from __future__ import division
from __future__ import print_function


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """

    """my_list = range(low, high)
    hi = len(my_list)
    lo = 0
    found = False
    tries = 0
    guesses = []
    while not found:
        mid = int((hi + lo) // 2)
        print (mid, my_list[mid])
        guesses.append(my_list[mid])
        if my_list[mid] == actual_number:
            tries += 1
            found = True
        elif hi == actual_number == lo:
            tries += 1
            found = True
        elif my_list[mid] > actual_number:
            hi = mid - 1
            tries += 1
        else:
            lo = mid
            tries += 1
    return {"guesses": guesses, "tries": tries}"""

    a = range(low, high)
    lo = 0
    hi = len(a) - 1
    guesses = []
    tries = 0
    found = False
    while not found:
        if a[lo] == actual_number or a[hi] == actual_number:
            guesses.append(actual_number)
            tries += 1
            found = True
            return {"guess": guesses, "tries": tries}
        else:
            mid = (lo + hi) // 2
            guesses.append(a[mid])
            if a[mid] == actual_number:
                tries += 1
                found = True
                return {"guess": guesses, "tries": tries}
            elif a[mid] < actual_number:
                lo = mid + 1
                tries += 1
            else:
                hi = mid
                tries += 1


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
