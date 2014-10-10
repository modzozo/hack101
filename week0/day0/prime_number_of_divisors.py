import is_prime
def prime_number_of_divisors(n):
	numDivisors = 0
	for iterate in range(1,n+1):
  		if n % iterate == 0:
		        numDivisors+=1	
	if is_prime.is_prime(numDivisors):
		return True
	else:	
		return False

def main():
        print (prime_number_of_divisors(12))

if __name__== '__main__':
        main()
	      
		

