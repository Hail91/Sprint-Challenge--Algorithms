'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    sub_str = 'th'  # <--- Substring we are searching for 

    if len(word) < 2:   # <---- Base case
        return 0
    elif word[0:2] == sub_str:   # If the first 2 characters of the world equal 'th', then...
        return count_th(word[len(sub_str) - 1:]) + 1   # Return the function recursively starting at the next character (Do not include first character in passed in word), also add 1 to the return to account for instances of 'th'
    else:
        return count_th(word[len(sub_str) - 1:])
        # Otherwise, return the function recursively starting at the next character but not returning any instances of 'th' since none were found
count_th('thatcher')
    

