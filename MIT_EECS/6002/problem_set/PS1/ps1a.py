###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import operator

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows = {}
    file = open(filename, 'r')
    Lines = file.readlines()
    for line in Lines:
        name, weight = line.split(',')[0], int(line.split(',')[1])
        cows[name] = weight
    file.close()
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    """
    # reverse order
    name_list = list(cows.keys())
    trips = []
    curr_trip = []
    curr_limit = limit
    while name_list:
        for name in reversed(name_list):
            if cows[name] <= curr_limit:
                curr_trip.append(name)
                curr_limit -= cows[name]
                name_list.remove(name)
        trips.append(curr_trip)
        curr_trip = []
        curr_limit = limit

    # normal order
    name_to_remove = []
    while name_list:
        for name in name_list:
            print(name)
            if cows[name] <= curr_limit:
                curr_trip.append(name)
                curr_limit -= cows[name]
                name_to_remove.append(name)
        for name in name_to_remove:
            name_list.remove(name)
        trips.append(curr_trip)
        curr_trip = []
        curr_limit = limit
        name_to_remove = []
    """

    cows_dict = cows.copy()
    trips = []
    while cows_dict:
        curr_trip = []
        curr_limit = limit
        descending_list = sorted(cows_dict.items(), key=operator.itemgetter(1), reverse=True)
        for name, weight in descending_list:
            if cows_dict[name] <= curr_limit:
                curr_trip.append(name)
                curr_limit -= cows_dict[name]
        for name in curr_trip:
            del cows_dict[name]
        trips.append(curr_trip)
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips_list = list(get_partitions(cows))
    min_trip = len(cows)
    chosen_trips = []
    for trips in trips_list:
        valid = True
        for trip in trips:
            if sum(cows[name] for name in trip) > limit:
                valid = False
                break
        if valid:
            if len(trips) < min_trip:
                min_trip = len(trips)
                chosen_trips = trips
    return chosen_trips
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    greedy_start = time.process_time()
    greedy_trips = greedy_cow_transport(cows)
    greedy_time = (time.process_time() - greedy_start)
    brute_start = time.process_time()
    brute_trips = brute_force_cow_transport(cows)
    brute_time = (time.process_time() - brute_start)
    print("Greedy method: number of trips" + str(len(greedy_trips)) + ", elapsed time:", greedy_time)
    print("Brute force method: number of trips" + str(len(brute_trips)) + ", elapsed time:", brute_time)