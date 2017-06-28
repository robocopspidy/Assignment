from wordfreqbigram import words_freq
 
sorted_words = words_freq.keys()
sorted_words.sort()

with open('tagcloudbigram.html', 'w') as f:
	f.write('''
		<html>
		<body>
		<script>
		function myFunction(text) {
			var w = window.open();
			w.document.open();
			w.document.write(text);
			w.document.close();
		}
		</script>
		''')

	for word in sorted_words:
		if len(words_freq[word][1]) > 1:
			f.write("""<font size='{}'><a href onclick= "myFunction({})" >{}</a></font>    """.format(words_freq[word][0],words_freq[word][1], word ))
	
	f.write('''
		</html>
		</body>
		''')

	
	
