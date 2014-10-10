import math
def sum_of_divisors(n):
	sum = 0
	for iterate in range(1,n+1):
		if n % iterate == 0:
			sum = sum + iterate
	return sum	
			
def main():
	print (sum_of_divisors(100000))

if __name__== '__main__':
	main()
