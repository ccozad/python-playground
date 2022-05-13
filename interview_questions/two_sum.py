# Two Sum asks you to find the index of two numbers in a list that add up to a given number
# A few rules are given to constrain the problem
# 1. An input has exactly one solution
# 2. The same element can't be used twice
# 3. The two indexes should be an array and can be in any order

# Before we get into the solution, let rule out a few options
# - We could just calculate all of the sums of every combination
# but this would baloon in complexity as the number of list 
# elements grew. So we need to find a way to simplify our search 
# space
# - We could search the list over and over again but this would
# be slow as the number of list elements increased. So we need a
# way to look up things fast.

# First let's look at a correct but unoptimized solution
def two_sum_v1(nums: list[int], target: int) -> list[int]:
    lookup = {}
    # Add every number in the search space to a dictionary
    # This maps the value to the index with a O(1) read
    for index, item in enumerate(nums):
        lookup[item] = index
        
    for index, item in enumerate(nums):
        # Reduce the amount of information to turn this into
        # a single variable problem
        second_number = target - item
        # Numbers in the lookup have been seen before
        if second_number in lookup:
            # An extra check to make sure we don't use the
            # same index.
            if lookup[second_number] != index:
                return [index, lookup[second_number]]

# That double loop is a little annoying. When I see the the same
# collection being itterated twice I always ask "can it be done in
# just one pass?". In this case it can!

# A one pass solution
def two_sum_v2(nums: list[int], target: int) -> list[int]:
    lookup = {}
    # This time we'll check the dictionary for past entires as we go
    # As an added bonus we can exit early once the answer is found
    # We also don't need the extra check to see if we are duplicating
    # an index.
    for index, item in enumerate(nums):
        second_number = target - item
        if second_number in lookup:
            return [index, lookup[second_number]]
        else:
            # Not the number we need, remember it for later
            lookup[item] = index