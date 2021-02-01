t = int(input())
import math
while t:
	flag = "b"
	size, limit = map(int, input().split())
	arr = list(map(int,input().split()))
	success = fail = 0
	for i in arr:
		if i!=-1:
			success+=1
	if success<math.ceil(size/2):
		print("Rejected")
	else:
		if max(arr)>limit:
			print("Too Slow")
		else:
			for i in arr:
				if i == 0 or i == 1:
					pass
				else:
					flag = "nb"
			if flag=="nb":
				print("Accepted")
			else:
				print("Bot")
	t-=1