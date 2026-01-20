#Iterative Statements
from ast import Continue

# For Loop

a = 1
for a in range(1000,100,-2):
    print(a)

# While Loop

n = 0
while n < 1000:
    print(n)
    n += 1

#Break
print("Break Statements")
for a in range(1,10):
    if a == 5:
        break
    print(a)

#Continue
print("Continue")
for a in range(1,10):
    if a == 5:
        Continue
        print(a)

#PASS
print("Pass")
for a in range(1,10):
    if a == 5:
        pass
    print(a)
