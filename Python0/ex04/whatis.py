from sys import argv

if len(argv) == 1:
	exit()
try: 
	assert 1 <= len(argv) <= 2, "more than one argument is provided"

	num = argv[1]

	numtrim = num.lstrip("-")
	assert numtrim.isdigit(), "argument is not an integer"
	if int(numtrim) % 2 == 0:
		print("I'm even")
	else:
		print("I'm odd")

except AssertionError as e:
	print("AssertionError:", e)