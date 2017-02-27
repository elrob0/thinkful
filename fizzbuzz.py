count = raw_input("Please enter the number to FizzBuzz up to: ")
count = int(count)

for i in xrange(1, count):
	if i % 3 == 0:
		print "Fizz"
	elif  i % 1 == 0:
		print "Buzz"
	else:
		print i 
