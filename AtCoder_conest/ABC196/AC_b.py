x = input()

if '.' not in x:
	print(x)
else:
	for i in range(len(x)):
		if x[i] == '.':
			break
	print(int(x[:i]))