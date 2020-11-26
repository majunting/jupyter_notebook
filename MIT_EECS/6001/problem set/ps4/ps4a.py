# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def swap_letter(sequence, pos):
    if pos != 0:
        new_str = sequence[pos] + sequence[1:pos] + sequence[0] + sequence[pos+1:]
    else:
        new_str = sequence
    return new_str

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    permutation_list = []
    if len(sequence) > 1:
        for i in range (len(sequence)):
            new_list = get_permutations(swap_letter(sequence, i)[1:])
            for j in new_list:
                permutation_list.append(sequence[i] + j)
    else:
        permutation_list.append(sequence)
    return permutation_list
    # pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    test_1 = 'def'
    test_2 = 'qwer'
    test_3 = 'abcde'
    print('Actual Output:', get_permutations(test_1))
    print('Actual Output:', get_permutations(test_2))
    print('Actual Output:', get_permutations(test_3))

