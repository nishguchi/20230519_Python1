# Python

s = "Hello World"
a = [1, 2, 3]

print("【処理：文字数を数える】")
print(str(s) + "【s】 の文字数は、" + str(len(s)))

print(str(a) + "【a】のリスト要素数は、" + str(len(a)))

print("\n")


n = [1, 2, 3, 4, 5]
print("【リスト処理：合計、最大、最大】")
print("リストn、", n)
print("リストn合計値は、", sum(n))
print("リストn最大値は、", max(n))
print("リストn最小値は、", min(n))

print("\n")


print("【処理：四捨五入 1】")
n = [1.1, 2.1, 3.1, 4.1]
m = sum(n)

print("リストn、", n)
print("リストn合計、", m)
print("四捨五入で【切り捨て】、", round(m))


print("\n")

print("【処理：四捨五入 2】")
n = [1.1, 2.1, 3.1, 4.1, 5.1]
m = sum(n)
print("リストn、", n)
print("リストn合計、", m)
print("四捨五入で【切り上げ】、", round(m))

print("\n")

print("【処理：四捨五入 3】")
print("5.4四捨五入で【切り捨て】、", round(5.4))
print("5.5四捨五入で【切り上げ】、", round(5.5))
