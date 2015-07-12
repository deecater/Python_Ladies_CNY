#Prompt the user for addresses
address1 = raw_input("Enter the first address: ")
address2 = raw_input("Enter the second address: ")
address3 = raw_input("Enter the third address: ")

#Make the address lowercase for easy testing
address1lower = address1.lower()
address2lower = address2.lower()
address3lower = address3.lower()

#Create a list for each quadrant
NWlist = []
NElist = []
SElist = []
SWlist = []

#Use 'in' to search for quadrants in the first address
if (" nw " in address1lower) == True:
	NWlist.append(address1)
elif (" ne " in address1lower) == True:
	NElist.append(address1)
elif (" se " in address1lower) == True:
	SElist.append(address1)
elif (" sw " in address1lower) == True:
	SWlist.append(address1)
else:
	print "First address is not in a quadrant"

#Use 'in' to search for quadrants in the second address
if (" nw " in address2lower) == True:
	NWlist.append(address2)
elif (" ne " in address2lower) == True:
	NElist.append(address2)
elif (" se " in address2lower) == True:
	SElist.append(address2)
elif (" sw " in address2lower) == True:
	SWlist.append(address2)
else:
	print "Second address is not in a quadrant"

#Use 'in' to search for quadrants in the thrid address
if (" nw " in address3lower) == True:
	NWlist.append(address3)
elif (" ne " in address3lower) == True:
	NElist.append(address3)
elif (" se " in address3lower) == True:
	SElist.append(address3)
elif (" sw " in address3lower) == True:
	SWlist.append(address3)
else:
	print "Third address is not in a quadrant"


#Print out the number of items and contents of each list
print "Number of address in NW quadrant:", len(NWlist), "\nAddresses in NW quadrant", NWlist
print "Number of address in NE quadrant:", len(NElist), "\nAddresses in NE quadrant", NElist
print "Number of address in SE quadrant:", len(SElist), "\nAddresses in SE quadrant", SElist
print "Number of address in SW quadrant:", len(SWlist), "\nAddresses in SW quadrant", SWlist
