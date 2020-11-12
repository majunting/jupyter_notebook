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

## Unable to pass all tests due to precision problem

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
    original_val, src_unit, dest_unit, error = check_error(command)
    if not error:
        conversion_rate = get_conversion_rate(src_unit, dest_unit)
        converted_val = original_val * conversion_rate
        print(original_val, src_unit + ' = %.6f' % converted_val + ' ' + dest_unit)

    # END OF YOUR CODE


# TODO: Add Other Functions Here
def check_error(command):
    error = True
    if not len(command.split()) == 4:
        print("Error: incorrect number of inputs")
    else:
        original_val, src_unit, check_str, dest_unit = command.split()
        # original_val = float(original_val)
        if not check_str == 'in':
            print("Error: incorrect input format")
        if not is_number(original_val):
            print("Error: 1st input is not numeric")
        else:
            error = False
            if original_val.isnumeric():
                original_val = int(original_val)
            else:
                original_val = float(original_val)
            return original_val, src_unit, dest_unit, error
    return 0, 0, 0, True

def get_conversion_rate(src_unit, dest_unit):
    dist_dict = {
                "m": 1,
                "ft": 3.2808398950131,
                "cm": 100,
                "mm": 1000,
                "mi": 0.00062137119223733,
                "yd": 1.0936132983377,
                "km": 0.001,
                "in": 39.370078740157
    }
    weight_dict = {
                "g": 1,
                "kg": 0.001,
                "lb": 0.00220462,
                "oz": 0.035274,
                "mg": 1000
    }
    volume_dict = {
                "mL": 1,
                "L": 0.001,
                "floz": 0.033814,
                "qt": 0.00105669,
                "cup": 0.00416667,
                "gal": 0.000264172,
                "pint": 0.00211338
    }
    if src_unit in dist_dict and dest_unit in dist_dict:
        conversion_rate = dist_dict[dest_unit] / dist_dict[src_unit]
    elif src_unit in weight_dict and dest_unit in weight_dict:
        conversion_rate = weight_dict[dest_unit] / weight_dict[src_unit]
    elif src_unit in volume_dict and dest_unit in volume_dict:
        conversion_rate = volume_dict[dest_unit] / volume_dict[src_unit]
    else:
        print("Error: incorrect unit inputs")
        return 0
    return conversion_rate

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

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
