# Given a String S, revers the string without reversing the words. Words are separated by periods.
def reverse_string(s):
    # Split the string into an array of words
    words = s.split('.')
    # Reverse the array of words
    words.reverse()
    # Join the array of words into a string
    s = '.'.join(words)
    # Return the string
    return s