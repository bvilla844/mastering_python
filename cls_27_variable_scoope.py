# variable scope = where a variable is visible and accessible
# scoop resolution = (LEGB) local -> enclose -> global -> built

from math import e

def func1():
    print(e)

e = 3
func1()
