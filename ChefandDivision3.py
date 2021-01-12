t = int(input())
while t:
	setter, req, time = map(int,input().split())
	problems = list(map(int,input().split()))
	total = sum(problems)
	p = total//req
	if p>time:
		print(time)
	else:
		print(p)
	t-=1
