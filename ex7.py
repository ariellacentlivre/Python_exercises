# prints the string
print "Mary had a litte lamb."

# prints the string that includes a string formatter, 
# at the end we tell it the string formatter is equal to snow
print "Its fleece was white as %s." % 'snow'

# print the string
print "And everywhere that Mary went."

# prints ten times the period so ten periods
print "." * 10 #what did that do? 

# setting these variables equal to a value that is a string
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end, try removing it to see what happens 
# prints the concatinated version of variables end1 through 6 and then adds a comma as a space
# prints the concatinated version of variables end7 through 12 with both on 1 line
# if you remove the comma Cheese is printed on 1 line with Burger on a second line
# if you remove the comma and put a + sign it prints CheeseBurger 
# if you put a comma after end6, end7 + end8... you get Cheese Burger, the same as doing print end1-6, print end7-12.. best practice
# longer than 80 characters is bad style in python

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

