# 関数をほかの関数の中で定義できる
'''
関数内関数を使う理由
1. 処理の分離：複雑な処理を分けて管理しやすくする。
2. コードの再利用：同じ処理を複数回呼び出す場合に再利用しやすくする。
3. スコープの限定：関数内でのみ使用されるロジックを外部に漏らさないようにする。
'''
def outer(x):
    def inner(y):
        return x + y
    return inner

adder = outer(5)
result = adder(8)
print(result)
# Output: 13

result = outer(7)(2)
print(result)
# Output: 9

# -------------------------
# 関数内で複数回実行される複雑な処理を実行したい時に役立つ
def knights(saying):
    def inner(quote):
        return f"We are the knights who say: '{quote}'"
    return inner(saying)
print(knights('Ni!'))
# Output: We are the knights who say: 'Ni!'

# -------------------------
# クロージャとしても機能する．クロージャとは，他の関数によって動的に生成される関数で，
# 自分の外で作られた変数の値を変えたり，覚えたりできる．
def knights2(saying):
    def inner():
        return f"We are the knights who say: '{saying}'"
    return inner

a = knights2('Duck')
b = knights2('Hasepfeffer')
print(a())
# Output: We are the knights who say: 'Duck'
print(b())
# Output: We are the knights who say: 'Hasepfeffer'
