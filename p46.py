# Python

# リスト
n = [1, 2, 4]

print("【リスト要素上書き】")
print("リストn",n)
n[2] = 3
print("n[2]インデックス2を、要素「3」で更新（上書き）")
print("リストn更新後、",n)

print("\n")

print("【リスト要素追加】")
n.append(4)
print("リストn末尾に要素「4」追加",n)
print("リストn",n)

print("\n")

print("【リストインデックス位置指定、要素追加】")
print("リストn先頭と末尾に要素【追加前】",n)

n.insert(0,0) # 第一引数でインデックス一指定、第二引数に要素内容記述
n.insert(5,5) # インデックス4の位置に、要素5を追加
print("リストn先頭と末尾に要素【追加後】 先頭「0」末尾「5」",n)

print("\n")


print("【リストの結合】")
n = [1, 2, 3] # n 内容を代入で上書き
m = [4, 5, 6]
v = n + m # リストを結合、代入
print("リストn",n)
print("リストm",n)
print("リストｎ、リストm結合出力",v)
v.append(7)
print("結合リストv末尾に要素7追加",v)

print("\n")

print("【リスト要素削除】")
print("リストv末尾要素削除【末尾要素削除前】", v)
del(v[6])
print("リストv末尾要素削除【末尾要素削除後】", v)
print("リストvインデックス3から5まで、削除【削除前】", v)
del(v[3:6])
print("リストvインデックス3から5まで、削除【削除後】", v)


print("\n")

print("【リスト要素数取得】")
print("リストvの要素数は、",len(n), "です")




