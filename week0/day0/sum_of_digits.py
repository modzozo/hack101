def sum_of_digits(number):
	for digit in str(number):
		sum=0
		absNumber=abs(number)
		while absNumber:
			sum += absNumber %10
			absNumber //=10
	return sum


def main():
	print (sum_of_digits(-52))

if __name__== '__main__':
	main()