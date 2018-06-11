def base36_to_base10(sample):
	num = 0
	#Check to see if sample is empty
	if not sample:
		#Its empty so we return error meesage
		return {"error":"Cannot convert empty string"}
	#store alphabet and numbers to user in conversion
	alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
				'P','Q','R','S','T','U','V','W','X','Y','Z']
	#Iterate over sample charater by character
	for i,s in enumerate(sample):
		#Check to see if the character is digit or character
		if s.isalnum():
			#If it is character or digit so we calculate
			num += alphabet.index(s.upper())*(36**(len(sample)-i-1))
		else: 
			#Otherwise its not so we return error
			return {"error":"Invalid character"}
	#Return data back
	return {"data":num}

if __name__ == '__main__':
	print(base36_to_base10(""))
