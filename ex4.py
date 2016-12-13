cars = 100 
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars,"cars available."

print "Thereare only", drivers, "drivers available"

print "There will be", cars_not_driven, "empty cars today."

print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "We need to put about", average_passengers_per_car, "in each car."

# difference between = (single equal) and == (double equal) : 
# single equal assigns the value on the right to a variable on the left, double equal compares if the two things have the same value
