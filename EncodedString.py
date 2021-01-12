def binaryToDecimal(binary):
	binary1 = binary = int(binary)
	decimal, i, n = 0, 0, 0
	while(binary != 0): 
		dec = binary % 10
		decimal = decimal + dec * pow(2, i) 
		binary = binary//10
		i += 1
	return decimal

t = int(input())
while t:
	quant = int(input())
	binary = input()
	result=''
	li=[]
	for i in range(0, len(binary), 4):
		encode = binaryToDecimal(binary[i:i+4])
		li.append(chr(97+encode))
	for i in li:
		result = result + i
	print(result)
	t-=1
