# 大きくなる可能性があるシーケンスを作りたい時は，ジェネレータ関数を書けば良い
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
print(type(my_range))
# Output: <class 'function'>

ranger = my_range(0, 10)
print(type(ranger))
# Output: <class 'generator'>

result = [i for i in ranger]
print(result)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result_again = [i for i in ranger]
print(result_again)
# Output: []

