# Python



# if文
print("【 if文 】")
a = 5

if(a >= 1):
	print("aは１より大きいです")

print("\n")

# if - else文
print("【 if - else文 】")
if(a >= 10 ):
	print("aは１より大きいです")
else:
	print("aは１０より小さいです")

print("\n")

# if - else if文
print("【 if - else if文 】")
if(a >= 10 ):
	print("aは１より大きいです")
elif(a == 5):
	print("aは５と等しいです")
else:
	print("aは１０より小さいです")


print("\n")

# if - else if文 条件分岐（倍数確認）
print("【 if - else if文  条件分岐（倍数確認） 】")
if(a % 2 == 0):
	print("aは2の倍数です")
elif(a % 3 == 0):
	print("aは3の倍数です")
else:
	print("aは2の倍数でも3の倍数でもありません")

