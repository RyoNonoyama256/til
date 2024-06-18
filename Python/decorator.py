# 引数のvalidationなどソースコードを変えずに関数に変更を行いたいとき，デコレータを用いる

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Results: ', result)
        return result
    return new_function

# -------------------
# 手動で修飾
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))
# Output: 8
cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))
''' Output:
Running function:  add_ints
Positional arguments:  (3, 5)
Keyword arguments:  {}
Results:  8
8
'''

# -------------------
# 自動で修飾
@document_it
def decorated_add_ints(a, b):
    return a + b

print(decorated_add_ints(3, 5))
''' Output
Running function:  decorated_add_ints
Positional arguments:  (3, 5)
Keyword arguments:  {}
Results:  8
8
'''

# -------------------
# デコレータは複数持てる
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# デコレータの順序が結果に影響する
@document_it
@square_it
def double_decorated_add_ints(a, b):
    return a + b

print(double_decorated_add_ints(3, 5))
''' Output
Running function:  new_function
Positional arguments:  (3, 5)
Keyword arguments:  {}
Results:  64
64
'''
