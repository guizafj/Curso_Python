from collections import namedtuple

CrateData = namedtuple('CrateData', ['houses', 'crates'])

def max_recycling(crates):
    """Returns the index with the largest value in the list and the number of crates for that house.
            Raises ValueError if list is empty."""
    if crates is None or len(crates) == 0:
        raise ValueError('A list with at least one element is required')
    max_houses = []
    max_crates = crates[0]
    for crate in crates:
        if crate > max_crates:
            max_crates = crate

    for house, crates in zip (range(len(crates)), crates):
        if crates == max_crates:
            max_houses.append(house)
        return CrateData(max_houses, max_crates)

def min_recycling(crates):
    """Returns the smallest value in the list  and a list of house number (list indexes) with that value.
    Raises ValueError if list is None or empty."""
    if crates is None or len(crates) == 0:
        raise ValueError('A list with at least one element is required')
    min_houses = []
    min_crates = crates[0]

    for crate in crates:
        if crate < min_crates:
            min_crates = crate

    for house, crates in zip (range(len(crates)), crates):
        if crates == min_crates:
            min_houses.append(house)
    return CrateData(min_houses, min_crates)

def total_crates(crates):
    """ Return the total of all the values in the crates list"""
    total = 0
    for crate in crates:
        total += crate
    return total

def get_crate_quantities(houses):
    """ Ask user for number of crates for each house"""
    crates = []
    for house in range(houses):
        crates.append(positive_int_input('Enter crates for house {}'.format(house)))
    return crates

def positive_int_input(question):
    """ Valdiate user enters a positive integer """
    while True:
        try:
            integer = int(input(question + ' '))
            if integer >= 0:
                return integer
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Please enter a positive integer.')

def main():
    print('Recycling truck program')
    houses = positive_int_input('How many houses?')
    crates = get_crate_quantities(houses)
    maximums = max_recycling(crates)
    minimums = min_recycling(crates)
    total = total_crates(crates)
    print('The total number of crates set out on the street is {}'.format(total))
    print('The max number of crates from any house is {}'.format(maximums.crates))
    print('The house(s) with the most recycling is {}'.format(maximums.houses))
    print('The min number of crates from any house is {}'.format(minimums.crates))
    print('The house(s) with the least recycling is {}'.format(minimums.houses))

if __name__ == '__main__':
    main()
