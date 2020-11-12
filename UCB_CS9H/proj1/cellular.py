import argparse


def decimal_to_binary(x):
    """
    This function converts a decimal number N into a binary number with 8 bits.
    :param x: The decimal number

    >>> decimal_to_binary(30)
    '00011110'
    >>> decimal_to_binary(139)
    '10001011'
    """
    assert 0 <= x <= 255
    # START OF YOUR CODE
    res = ""
    for i in range (0, 8):
        if (x >= (2 ** (7 - i))):
            res = res + "1"
            x -= 2 ** (7 - i)
        else:
            res = res + "0"
    return res

    # END OF YOUR CODE


def generate(rule, steps):
    """
    Generate the image from given rule number and steps
    and print it to the console.
    The output image should have width of 2 * STEPS + 1 and height of STEPS + 1.

    :param rule: The rule number
    :param steps: Number of lines

    >>> generate(30, 5)
    P1 11 6
    0 0 0 0 0 1 0 0 0 0 0
    0 0 0 0 1 1 1 0 0 0 0
    0 0 0 1 1 0 0 1 0 0 0
    0 0 1 1 0 1 1 1 1 0 0
    0 1 1 0 0 1 0 0 0 1 0
    1 1 0 1 1 1 1 0 1 1 1
    """
    # START OF YOUR CODE
    rule_str = decimal_to_binary(rule)

    rule_dict = {
        0: rule_str[7],
        1: rule_str[6],
        2: rule_str[5],
        3: rule_str[4],
        4: rule_str[3],
        5: rule_str[2],
        6: rule_str[1],
        7: rule_str[0]
    }

    # param line
    print("P1 ", 2 * steps + 1, " ", steps + 1)
    # 1st line, only center is 1
    curr_line = ""
    for idx in range (2 * steps + 1):
        if (idx == steps):
            curr_line += "1"
        else:
            curr_line += "0"
    print_line(curr_line)
    prev_line = curr_line
    if wolfram:
        # brute force way to achieve wolfram
        # instead of considering as an infinite grid, expand by n grids (n == steps)
        prev_line += "0" * steps
        for line in range (steps):
            curr_line = ""
            for idx in range (2 * steps + 1 + steps):
                if (idx == 0):
                    curr_line += get_char_val(rule_dict, prev_line[:2])
                elif (idx == 2 * steps + steps):
                    curr_line += get_char_val(rule_dict, prev_line[-2:] + "0")
                else:
                    curr_line += get_char_val(rule_dict, prev_line[idx-1:idx+1] + prev_line[idx + 1])
            print_line(curr_line[:-steps])
            prev_line = curr_line
    else:
        # 2nd line onwards
        for line in range (steps):
            curr_line = ""
            for idx in range (2 * steps + 1):
                if (idx == 0):
                    curr_line += get_char_val(rule_dict, prev_line[:2])
                elif (idx == 2 * steps):
                    curr_line += get_char_val(rule_dict, prev_line[-2:] + "0")
                else:
                    curr_line += get_char_val(rule_dict, prev_line[idx-1:idx+1] + prev_line[idx + 1])
            print_line(curr_line)
            prev_line = curr_line

    # END OF YOUR CODE


# TODO: You may add any additional functions here
def get_char_val (rule_dict, str):
    decimal_val = binary_to_decimal(str)
    return rule_dict[decimal_val]


def binary_to_decimal(decimal_str):
    res = 0
    for i in range(len(decimal_str)):
        if (decimal_str[i] == '1'):
            res += 2 ** (len(decimal_str) - i - 1)
    return res

def print_line(str):
    new_str = ""
    for idx in range(len(str) - 1):
        new_str += str[idx] + ' '
    new_str += str[-1:]
    print(new_str)

if __name__ == '__main__':
    # START OF YOUR CODE
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('Rule',
                        type = int)
    parser.add_argument('Steps', 
                        type = int)
    parser.add_argument('--wolfram',
                        action = 'store_true',
                        default = False)

    args = parser.parse_args()
    rule, steps = args.Rule, args.Steps
    wolfram = args.wolfram

    # END OF YOUR CODE

    assert 0 <= rule <= 255 and steps >= 0
    generate(rule, steps)
