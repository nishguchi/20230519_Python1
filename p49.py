# Python

# dict 辞書
# ハッシュテーブル
# キーでバリュー指定する

a = {1:"one",2:"two",3:"three"}
b = {"r":100,"g":200,"b":300}


print("【辞書要素 追加、更新】")

print("リストa【追加更新前】",a)
print("リストb【追加更新前】",b)

a[1] = "ワン" # キー名があるので、更新される
a[4] = "フォー" #キー名がないので追加される
b["a"] = "追加分"  # キー名がないので、追加される

print("リストa【追加更新後】",a)
print("リストb【追加更新後】",b)

print("\n")

print("【辞書要素削除】")
del(b["a"])
print("リストb【削除後】",b)

print("\n")


print("【キーやアイテム値を、列挙して確認】")
print(a.keys())
print(a.values())
print(a.items())
# print(a.index()) インデックスはないので、エラー




