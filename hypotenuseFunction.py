leg1 = [3, 5, 7, 9]
leg2 = [4, 12, 24, 40]

def getHypotenuse(leg1, leg2):
	output = []
	for i in range(len(leg1)):
		output.append((leg1[i]**2 + leg2[i]**2)**0.5)
	return output

hypos = getHypotenuse(leg1, leg2)
for i in hypos:
	print(i)