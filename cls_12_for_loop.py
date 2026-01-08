# for loops = execute a block of code a fixed number of times

"""
for x in range (1,11):
    print (x)

for x in reversed (range(1,10)):
    print (x)
print ("happy new year")
"""
"""
str_var = "a string"
count = 0
for c in str_var:
    count += 1
print(count)
"""
"""
word = "hello world my name is brayan"
count = 0
for c in word:
    if c == " ":
        count += 1
print(count)
"""
n1 = 2
n2 = 8
for i in range(n1,n2+1):
    if i%2 ==0:
        print(i, end=" ")
print()
for i in reversed(range(n1,n2+1)):
    if i%2 ==1:
        print(i, end=" ")

