def unique_count_words(arr):
	set1= set()
	for iterate in arr:
		set1.add(iterate)
		result=len(set1)
	return result

def main():
	arr=["HELLO!"] * 10
	print (unique_count_words(arr))

if __name__== '__main__':
    main()
