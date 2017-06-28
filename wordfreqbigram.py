from clearnwords import cleanwords

words_freq = {}
new_words = []
#Generating dictionary(Words frequency) having word pair as key and frequency, lines in which word pair is present as values.
with open('textfile.txt', 'r') as f:
	
	text = f.read()
	words = cleanwords(text)
	i = 0
	while i< len(words)-1:
		new_words.append((words[i], words[i+1]))
		i += 1
	for word in new_words:
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
			if i[0]+' '+ i[1] in j:
				j = j.replace('\n', '<hr/>')
				words_freq[i][1].append(j)

				


