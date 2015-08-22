# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.


bread = 10
pb = 10
jelly = 4
closed_bread = bread/2
turn = 0

while closed_bread >=1 and pb >=1 and jelly >=1:
	turn = turn + 1
	print "Making Sandwich #{0}".format(turn)
	closed_bread = closed_bread-1
	pb = pb -1
	jelly = jelly -1
	print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(closed_bread, pb, jelly)
if closed_bread == 0 and pb >= 1 and jelly >= 1:
	print "All done! Only had enough bread for {0} sandwiches.".format(turn)
elif closed_bread >=1 and pb >=1 and jelly == 0:
	print"All done! I rant out of jelly!"
elif closed_bread >=1 and pb == 0 and jelly >=1:
	print "All done! I rane out of peanut butter!"
else:
	print "All done"
