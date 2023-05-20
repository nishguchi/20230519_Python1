# Python

f = 0.0
print("【f = f + 0.1 ループ】")
while(True):
	print(f)
	if(f >= 1):
		break
	f = f + 0.1	
print("\n break") # 誤差ある

print("\n")

f = 0.0
print("【f += 0.1 ループ】")
while(True):
	print(f)
	if(f >= 1):
		break
	f += 0.1	
print("\n break") # 誤差ある
