# Python

# 辞書 dict 
# キーとバリューで管理

a = {1:"zero", 2:"one", 3:"two", 4:"three", 5:"four"}

# for文 (リストループ)
print("【キーとバリュー表示】")	
for key, value in a.items():
#	print(index, n) # インデックスはありません【エラー】
	print(key, value)	

print("\n")


# for文 (リストループ)
print("【キーのみ表示】")	
for key, value in a.items():
	print(key)	

print("\n")


# for文 (リストループ)
print("【バリューのみ表示】")	
for key, value in a.items():
#	print(index, n) # インデックスはありません
	print(value)	

print("\n")






