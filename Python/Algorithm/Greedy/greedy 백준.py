# 5585
m = int(input())
n = 1000 - m

result = 0
list = [500, 100, 50, 10, 5, 1]

for coin in list :
    result += n//coin
    n %= coin
print(result)

# 10162
n = int(input())
if n%10 != 0:
	print(-1)
else:
	for i in [300, 60, 10]:
		print(n//i, end=' ')
		n = n%i

# 4796
i = 1

while True:
  result = 0
  L, P, V = map(int, input().split())
  
  if L + P + V == 0:
    break

  result = ((V//P) * L) + min((V%P), L)
  print("Case {}: {}".format(i, result))
  i += 1

# 2864 
# 1일1커밋 힘들다

# 2720

# 2810

# 14659

# 14720

# 14487

# 11034

# 22864

# 17224

# 18234

# 15881

# 21414

# 25176