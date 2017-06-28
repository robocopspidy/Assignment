
def get_words(text):
	'''take a string, parse it and return words.'''
	return text.split()

def cleanwords(text):
	'''Cleanwords removes punctuation, removes words which are just numbers, convert all words to lower case and return them. '''
	tmp = []
	for c in text:
		if c.isalpha():
			tmp.append(c.lower())
		
		elif c == ' ':
			tmp.append(' ')
		
	return ''.join(tmp).split()
	#return ''.join((c.lower() if c.isalpha() else ' ') for c in text).split()
	
#print(cleanwords("This is :an 5454 4541521 11212 ex44ample...!"))
