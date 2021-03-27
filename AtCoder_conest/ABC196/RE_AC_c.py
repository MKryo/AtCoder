n = int(input())
count=0

for i in range(1,1000001): #後半全てのループ
	x = int(str(i) * 2)
	if x <= n :
		count+=1
	else:
		break

print(count)

