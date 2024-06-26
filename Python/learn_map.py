
l = list(range(10))

def calculator(num):
    return num*2

l2 = map(calculator, l)

print(l2)
# Output: <map object at 0x110030fa0>
print(list(l2))
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# ---------------

l = list(range(10))
l2 = list(range(10))

def calculator2(x, y):
    return x * y

l3 = map(calculator2, l, l2)
print(list(l3))
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
