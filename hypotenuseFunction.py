# ----VARIABLES----
leg1 = [3, 5, 7, 9]
leg2 = [4, 12, 24, 40]

# ----METHODS----
# Hypotenuse Function
# PRECONDITION: inputs are same length
def getHypotenuse(leg1, leg2):
	output = [] # init output array
	for i in range(len(leg1)): # iterate through each value
		calculatedValue = (leg1[i]**2 + leg2[i]**2)**0.5
		output.append(calculatedValue) # calculate for hypotenuse and add to output list
		print(calculatedValue)
	return output

# -----RUNTIME----
hypos = getHypotenuse(leg1, leg2) # calculate list of hypotenuses
for i in hypos: # iterate through each value in list
	print(i) # print said value