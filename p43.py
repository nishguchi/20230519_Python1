# Python

# リスト
m = [1, 2, 3]
n = [1, 2.0, "3"] # 整数、小数、文字列、リスト混在可能

print("変数m",m)
print("mの型タイプは" , type(m))

print("変数n",n)
print("nの型タイプは",type(n))
print("\n")

# リスト要素の型を確認
print("n[0]の型タイプは",type(n[0]))
print("n[1]の型タイプは",type(n[1]))
print("n[2]の型タイプは",type(n[2]))
print("\n")

# リスト後ろから要素指定
print("リストn要素出力",n)
print("リスト後ろから要素指定出力")
print("n[-3]でn[0]出力",n[-3])
print("n[-2]でn[2.0]出力",n[-2])
print("n[-1]でn[0]出力",n[-1])

