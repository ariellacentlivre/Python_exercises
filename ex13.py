# Writing a script that accepts agruments 

from sys import argv

# ^ this is called input- this is how you
# add features to your script from the python feature set
# says what you plan to use
# "import the sys module"

# argv is agrument variable, holds the arguments you pass to python script when you run it

script, first, second = argv 

age = raw_input("How old are you? ")
name = raw_input ("What is your name? ")
# unpacks agrv so that gets assigned to four variables you can work with 
# "take whatever is in argv, unpack it, assign it to these variables on the left in order"

print "The script is called: ", script 
print "Your first variable is: ", first
print "Your second variable is: ", second 

print "you are %r" % (age)
print "Hello, %r" % (name)

# print as normal