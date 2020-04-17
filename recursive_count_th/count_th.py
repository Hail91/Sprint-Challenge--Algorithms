'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    sub_str = 'th'

    if len(word) < 2:   # <---- Base case
        return 0
    elif word[0:2] == sub_str:
        return count_th(word[len(sub_str) - 1:]) + 1
    else:
        return count_th(word[len(sub_str) - 1:])

count_th('thatcher')
    

