# pythonでは関数もオブジェクト

def greet(name):
    return f"Hello, {name}!"
# 関数を変数に代入
greet_function = greet
print(greet_function("Ryo"))
# Output: Hello, Ryo!

# ---------------------------
# 関数をリストに格納
function_list = [greet_function, lambda x: f"Hi, {x}!"]
for func, name in zip(function_list, ["Ryo", "Yuuki"]):
    print(func(name))
''' Output:
Hello, Ryo!
Hi, Yuuki!
'''

# ---------------------------
# 関数を他の関数に渡す
def call_function(func, argument):
    return func(argument)
result = call_function(lambda x: x[0] + x[1], [2 , 4])
print(result)
# Output: 6

# ---------------------------
# 関数を辞書に格納
function_dict = {
    'greet': greet_function,
    'shout': lambda x: f"{x.upper()}!!!"
}
result1 = function_dict["greet"]("Ryo")
result2 = function_dict["shout"]("echo")
print(result1, result2)
# Output: Hello, Ryo! ECHO!!!
