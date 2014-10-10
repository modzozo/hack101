def reduce_file_path(path):
	path= path.split('/')
	result= []
	for i, item in enumerate(path):
		if item =='..':
			del path[i]
	return ''.join(result)
	
def main():
	print (reduce_file_path("/home/birdy")

if __name__== '__main__':
    main()
