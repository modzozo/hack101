def nth_fibonacci(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return nth_fibonacci(n-1) + nth_fibonacci(n-2)

def main():
	print (nth_fibonacci(60))

if __name__== '__main__':
	main()

