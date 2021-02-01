t = int(input())
while t:
	x = list(map(int, input().split()))
	x.sort()
	if(x[0]+x[1]==x[2]):
		print("YES")
	else:
		print("NO")
	t-=1