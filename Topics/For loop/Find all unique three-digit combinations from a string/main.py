# Import statement
from itertools import permutations

# Define a function that takes a string of digits as input
def find_three_digit_combinations(digits):
    # Empty placeholder for holding the combinations
    combinations = []

    # :::TO BE COMPLETED:::

    # Return the combinations in ascending order without duplicates
    return sorted(list(set([''.join(i) for i in combinations if len(i) == 3])))

# You can test your function by calling it with a string of digits
print(find_three_digit_combinations('123'))