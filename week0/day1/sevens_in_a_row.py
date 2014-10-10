import itertools
def sevens_in_a_row(arr,n):
	in_a_row={}
	for iteration in arr:
		if arr[iteration]==arr[iteration+1]:
			print blaaa
			

def main():
	n=3
	arr=['1','1','1','2','3','-4']
	print (sevens_in_a_row(arr,n))

if __name__== '__main__':
    main()