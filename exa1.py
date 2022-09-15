import numpy as np
import sys
m = 0
while (m < 3):
	m = int(input("dimension de la matriz mayor o igual a 3 \n"))
a = np.zeros((m,m))
limit = m*m
prime = 2
count = 0
while count < limit :
	if prime > 1:
		for i in range(2, prime):
			if (prime % i) == 0:
				prime = prime+1
				break							
		else:			
			a[int(count/m)][int(count%m)] = prime
			prime = prime+1								
			count = count+1
suma = 0
for i in range(0,m):
	for j in range(0,m):		
		print("%4d" % a[i][j] , end = ' ')
		if(j >= i):
			suma = suma + a[i][j]
	print("\n")

print ("la suma de los elementos en la matriz diagonal superior es:",suma)


