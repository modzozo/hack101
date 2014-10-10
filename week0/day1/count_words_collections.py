import collections 

def count_words(arr):
	col=collections.Counter(arr)
	print(col)

def main():

	arr=['a','b','c','a']
	print (count_words(arr))

if __name__== '__main__':
    main()
