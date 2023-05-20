# Python

# While文 (ループ)
# 中断処理

n = 0
print("【中断処理】")
while(True):
	if n == 10:
		break
	n = n + 1
print("break!")


# for文
# 処理継続
print("【処理継続 奇数】")
for n in range(10):
	if n % 2 == 0:
		continue
	print("奇数:"+ str(n))

# for文
# 処理継続
print("【処理継続 偶数】")
for n in range(11):
	if n == 0:
		continue
	elif n % 2 != 0:
		continue
		print("偶数:"+ str(n))
	else:
		print("偶数:"+ str(n))




