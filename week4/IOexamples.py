"""IO examples.

Using file IO, from the docs:
    "The first argument is a string containing the filename. The second
    argument is another string containing a few characters describing the
    way in which the file will be used. mode can be 'r' when the file will
    only be read, 'w' for only writing (an existing file with the same name
    will be erased), and 'a' opens the file for appending; any data written
    to the file is automatically added to the end. 'r+' opens the file for
    both reading and writing. The mode argument is optional; 'r' will be
    assumed if it's omitted."
https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

"""
from __future__ import division
from __future__ import print_function
import json


def be_cool(name):
    """Just print, not actually doing any IO."""
    print(name + " is cool")


be_cool("Stephen")


def be_cool_for_ever(name, file_path):
    """Save a message about being cool for ever."""
    mode = "w"  # from the docs
    history_book = open(file_path, mode)
    history_book.write(name + " is cool")
    history_book.close()


be_cool_for_ever("Stephen", "Stephen_is_cool.txt")
be_cool_for_ever("Stephen", "week4/Stephen_is_cool.lol_UR_joking")
be_cool_for_ever("Stephen", "code1161base/week4/Stephen_is_cool.periscope")


def who_is_cool(file_path):
    """Read a file and print what it says."""
    mode = "r"  # from the docs
    history_book = open(file_path, mode)
    response = history_book.read()
    message = "historians have recorded that:\n\t"
    print(message + response)
    history_book.close()


who_is_cool("ben_is_cool.txt")


# some JSON examples:


def bury_time_capsule(something_for_your_kids_to_find, file_path):
    """Save some json to a file.

    Args:
        something_for_your_kids_to_find (dict): A dictionary of facts.
        file_path (str): The path to where you want to save the json.
    """
    try:
        dumped = json.dumps(something_for_your_kids_to_find)
        mode = "w"  # from the docs
        time_capsule = open(file_path, mode)
        time_capsule.write(dumped)
        time_capsule.close()
        return True
    except Exception as e:
        print(e)
        return False


message_for_capsule = {"name": "Stephen",
                       "Year": 2017,
                       "Location": "Sydney",
                       "Greeting": "Doing lad",
                       "Reply": "Not much lad " +
                               "Uni " +
                               "work",
                       "Alphabet Inc Class A": "847.80USD",
                       "fruit": ["apple", "apricot", "avocado", "abiu"]}

bury_time_capsule(message_for_capsule, "code1161base/week4/burying_capsule.")


def dig_up_capsule(file_path):
    """Read some json from a file.

    Does some defensive programming as an example of how you'd do such a thing.
    Args:
        file_path (str): The path to where you want to save the json.
    """
    try:
        mode = "r"  # from the docs
        time_capsule = open(file_path, mode)
        contents = json.load(time_capsule)
        time_capsule.close()
        keys_needed = ["Greeting", "Year", "Reply"]
        if all(key in contents for key in keys_needed):
            template = """{Greeting},\nDid you know that in {Year}, "{Reply}" was still true!
                       """
            print(template.format(**contents))
            return True
        else:
            print("Your dictionary is missing some keys.",
                  contents,
                  keys_needed)
            return False
    except Exception as e:
        print(e)
        return False


dig_up_capsule("under_the_patio.json")