import math
def is_prime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1,2):
		if n % x == 0:
			return False
	return True

def main():
	print (is_prime(11))

if __name__== '__main__':
	main()	
