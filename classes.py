def convert(string):
	a_dict = {}
	count = 0
	for i in string:
		if string.count(i) > 1:
			count += 1
			a_dict[i] = count
		else:
			a_dict[i] = 1
	return a_dict

print(convert("stringss"))