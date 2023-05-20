# Python

# dict 辞書
# ハッシュテーブル
# キーでバリュー指定する

a = {1:"one",2:"two",3:"three"}
b = {"r":100,"g":200,"b":300}
c = {"l":"エル","a":"エー","b":"ビー"}
d = {1:"one","r":100,"r":"rrr"}

x = {1:"one"}
y = {"r":100}
z = {"r":"rrr"}
x_1 = {1:100}  # タイプはdict

print("【辞書 a出力】")
print(a)
#print(a[0])  インデックス0はない【エラー】
print(a[1]) # インデックス = キー指定
print(a[2])
print(a[3])

print("\n")

print("【辞書 b出力】")
print(b)
print(b["r"]) # キーが文字列 "キー名" で指定
print(b["g"])
print(b["b"])

print("\n")

print("【辞書 c出力】")
print(c)
print(c["l"])
print(c["a"])
print(c["b"])

print("\n")

print("【辞書 d出力】")
print(d)
print(d[1])
print(d["r"]) # "r" = 100  出力時には、"rrr"上書きされている  (2つめ要素)
print(d["r"]) # "rrr" (3つめ要素)

print("\n")

print("【辞書タイプを確認】")
print(type(a))	 # タイプはdict
print(type(b)) 	# タイプはdict
print(type(c))  # タイプはdict
print(type(d))  # タイプはdict
print(type(x))  # タイプはdict
print(type(y))  # タイプはdict
print(type(x_1))  # タイプはdict
