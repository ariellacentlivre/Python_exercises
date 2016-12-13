# setting x variable equal to a string containing a raw data value, 
# at the end of the string we use the formatter to state the raw data value
x = "There are %r types of people." %10.023

# setting the binary variable equal to a string
binary = "binary"

# setting the do_not variable equal to a string
do_not = "don't"

# setting the y value equal to a string which contains two string formatters
# at the end of the string, we use the formatter to insert these values into the variable string
y = "Those who know %s and those who %s" % (binary, do_not)

# print the variable x
print x

#print the variable y
print y

# print the string with the raw data formatter, at the end we tell it the raw data formatter is x
print "I said: %r." %x

# print the string with the string formatter, at the end we tell it the string formatter is y
print "I also said: '%s'." %y

# setting the variable hilarious equal to a boolean value true
hilarious = True 

# setting the variable joke_evaulation equal to a string with a string formatter included in the quotes
joke_evaulation = "Isn't that joke so funny?! %s"

# print to the console, the string with the answer being the variable hilarious
print joke_evaulation %hilarious 

# setting the variable w equal to a string
w = "This is the left side of ..."

# setting the varialble e equal to a string
e = "a string with a right side."

# printing w plus e will concatinate the two strings (bring them together to make one string)
print w + e


