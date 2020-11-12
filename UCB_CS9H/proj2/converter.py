import sys

def print_banner():
    """
    Print the program banner. You may change the banner message.
    """
    # START OF YOUR CODE
    print("""
Welcome to our Python-powered Unit Converter v1.0 by JT!
You can convert Distances, Weights, Volumes to one another, but only
within units of the same category, which are shown below. E.g.: 1 mi in ft

   Distances: ft cm mm mi m yd km in
   Weights: lb mg kg oz g
   Volumes: floz qt cup mL L gal pint
""")
    # END OF YOUR CODE


def convert(command):
    """
    Handle a SINGLE user input, which given the command, either print
    the conversion result, or print an error, or exit the program.
    Please follow the requirements listed on project website.
    :param command: User input

    >>> convert("1 m in km")
    1 m = 0.001000 km
    """
    # START OF YOUR CODE
    if (command == "q"):
        print("Program shutting down")
        sys.exit()
    if 

    # END OF YOUR CODE


# TODO: Add Other Functions Here


###########################################
# DO NOT MODIFY ANYTHING BELOW
###########################################

def get_user_input():
    """
    Print the prompt and wait for user input
    :return: User input
    """
    return input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ")


if __name__ == '__main__':
    print_banner()
    while True:
        command = get_user_input()
        convert(command)
