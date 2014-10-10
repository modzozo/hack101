def sevens_in_a_row(arr,n):
	sevens=0
	for number in arr:
		if number ==7:
			sevens+=1
		elif sevens==n:
			return True
		else:
			n =0
	return False

def main():
	n=3
	arr=['1','1','1','2','3','-4','7','7','7']
	print (sevens_in_a_row(arr,n))

if __name__== '__main__':
    main()
