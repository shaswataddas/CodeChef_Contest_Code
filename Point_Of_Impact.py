t = int(input())
while t:
	n,k,x,y = map(int, input().split())
	if x==y:
		x=y=n
	elif x>y:
		if k%4==1:
			y = y+n-x
			x = n
		elif k%4==2:
			x = n-(x-y)
			y =	n
		elif k%4==3:
			y = abs(y-x)
			x = 0
		else:
			x = x-y
			y = 0
	else:
		if k%4==1:
			x = x+n-y
			y = n
		elif k%4==2:
			y =	n-(y-x)
			x = n
		elif k%4==3:
			x = abs(x-y)
			y = 0
		else:
			y = y-x
			x = 0  
	print(x,y)
	t-=1
