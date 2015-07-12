# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.


# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

bread = 7
pb = 3
jelly = 0
closed_bread = bread/2
open_bread = bread % 2
odd_pb = pb % 2
odd_jelly = jelly % 2
pb_no_jelly = pb - jelly

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich";
#		If you don't; print a message like "Looks like I don't have a lunch today"

if bread >= 2 and pb >= 1 and jelly >= 1:
	if closed_bread >= 2 and pb >= closed_bread and jelly >= closed_bread:
		print "I can make", closed_bread, "peanut butter and jelly sandwiches."
# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before
	elif closed_bread >= 2 and closed_bread > pb and pb < jelly and pb > 1:
		print "I can make", pb, "peanut butter and jelly sandwiches."
# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches
	elif closed_bread >=2 and closed_bread > jelly and jelly < pb and jelly > 1 and pb_no_jelly >= 1:
		print "I can make", jelly, "peanut butter and jelly sandwiches. I can also make", pb_no_jelly, "peanut butter sandwiches."
	elif closed_bread >=2 and closed_bread > jelly and jelly < pb and jelly > 1:
		print "I can make", jelly, "peanut butter and jelly sandwiches."
	else:
		print "I can make a peanut butter and jelly sandwich."
elif bread ==1 and pb >= 1 and jelly >= 1:
	print "I can't make a full sandwich, but I can make an open-face sandwich."
# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.
elif bread < 1:
	print "Out of bread. Can't make a lunch today. :("
elif pb < 1:
	print "Out of peanut butter. Can't make a lunch today. :("
elif bread >=2 and pb >1 and jelly < 1:
	print "Hmmm...I can't make a peanut butter and jelly sandwich, but I can at least make a sad peanut butter sandwich."
else:
	print "Oops. Can't make a lunch today."
# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py
if bread > 1 and open_bread == 1 and odd_pb == 1 and odd_jelly == 1:
	print "I can also make an open-face sandwich! Lucky!"



