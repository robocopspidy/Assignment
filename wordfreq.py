from clearnwords import cleanwords

words_freq = {}
#Generating dictionary(Words frequency) having word as key and frequency, lines in which word is present as values.
with open('textfile.txt', 'r') as f:
	
	text = f.read()
	words = cleanwords(text)
	for word in words:
		if word in words_freq:
			words_freq[word][0] += 1
		else:
			words_freq[word] = [1,[]]

#Removing noise words form words_freq dictionary.
with open('noisewords.txt', 'r') as f:
	noises = f.read().split()

	for noise in noises:
		if noise in words_freq:
			del words_freq[noise]

#finding lines which contain words and appending then in words_freq dictionary.
with open('textfile.txt', 'r') as f:
	lines = f.readlines()
	for i in words_freq:
		for j in lines:
			if i in j:
				j = j.replace('\n', '<hr/>')
				words_freq[i][1].append(j)
				


