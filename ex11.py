print "How old are you?",
age = raw_input()
print "How tall are you?", 
height = raw_input()
print "How much do you weigh", 
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy" % (
	age, height, weight)

# raw_input() presents a prompt to the user, gets input from the user, and returns the data input by the user in a string

name = raw_input("What is your name? "),
print "Hello, %s." % name