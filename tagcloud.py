from wordfreq import words_freq
 
sorted_words = words_freq.keys()
sorted_words.sort()

with open('tagcloud.html', 'w') as f:
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
		f.write("""<font size='{}'><a href onclick= "myFunction({})" >{}</a></font>    """.format(words_freq[word][0],words_freq[word][1], word ))
	
	f.write('''
		</html>
		</body>
		''')

	
	
