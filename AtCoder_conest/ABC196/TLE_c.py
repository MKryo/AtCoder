n = int(input())
count=0

for i in range(1,n+1):
	s = str(i)
	l = len(str(i))
	if l % 2 == 0:
		p = int(l/2)	
		if s[:p] == s[p:]:
			count+=1

print(count)

#全探索しちゃってるので時間かかりすぎ
#O(N)