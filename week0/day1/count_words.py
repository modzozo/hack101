def count_words(arr):
	result= {}
	for iterate in arr:
		
		result[iterate]=arr.count(iterate)
	return result

def main():
	arr=['a','b','c','a','a','b']
	print (count_words(arr))

if __name__== '__main__':
    main()
