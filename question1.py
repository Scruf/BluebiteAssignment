def base36_to_base10(sample):
	num = 0
	alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
				'P','Q','R','S','T','U','V','W','X','Y','Z']
	for i,s in enumerate(sample):
		num += alphabet.index(s.upper())*(36**(len(sample)-i-1))
	print(num)

if __name__ == '__main__':
	base36_to_base10("ixqye")
