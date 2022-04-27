# This interview question challenges the candidate to swap two numbers
# without using a third variable to do the swap. Unless you are going for
# some type of low level embedded job you are never going to need to be
# this clever in your daily coding. Consider this type of question to be
# the interviewer wanting to make you sweat.

# We'll make a function so we can test our work
def swap(items):
    # If we were being funny we would just call reverse() on items...
    #
    # We can use some properties of addition for this puzzle. Our starting
    # state is:
    # [0] = A, [1] = B
    items[0] = items[0] + items[1] # [0] = A + B, [1] = B
    items[1] = items[0] - items[1] # [0] = A + B, [1] = A + B - B = A
    items[0] = items[0] - items[1] # [0] = A + B - A = B, [1] = A