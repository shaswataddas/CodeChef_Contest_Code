'''
Elections are coming soon. This year, two candidates passed to the final stage. One candidate is John Jackson and his opponent is Jack Johnson.

During the elections, everyone can vote for their favourite candidate, but no one can vote for both candidates. Then, packs of votes which went to the same candidate are formed. You know that for John Jackson, there are N
packs containing A1,A2,…,AN votes, and for Jack Johnson, there are M packs containing B1,B2,…,BM

votes.

The winner is the candidate that has strictly more votes than the other candidate; if both have the same number of votes, there is no winner. You are a friend of John Jackson and you want to help him win. To do that, you may perform the following operation any number of times (including zero): choose two packs of votes that currently belong to different candidates and swap them, i.e. change the votes in each of these packs so that they would go to the other candidate.

You are very careful, so you want to perform as few swaps as possible. Find the smallest number of operations you need to perform or determine that it is impossible to make John Jackson win.

Example Input

2
2 3
2 2
5 5 5
4 3
1 3 2 4
6 7 8

Example Output

2
1

'''
def isJohnWins(john, jack, sum_john, sum_jack, c):
    get_answer = 0
    if sum_jack < sum_john:
        return 0
    else:
    	while True:
		    #jack_max = max(jack)
		    #john_min = min(john)
		    if jack==[] or john==[]:
		    	break
		    jack_max = jack[0]
		    john_min = john[0]
		    jack.remove(jack_max)
		    john.remove(john_min)
		    diff = jack_max - john_min
		    sum_jack = sum_jack - diff
		    sum_john = sum_john + diff
		    c+=1
		    if sum_john>sum_jack:
		    	get_answer = 1
		    	break
    	if get_answer==1:
    		return c
    	else:
    		return -1

t = int(input())
while t:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    sum_a = sum(a)
    sum_b = sum(b)
    print(isJohnWins(a, b, sum_a, sum_b, 0), end='\n')
    t -= 1
