def pig_latin_converter(word):
	vowels = ['a', 'e', 'i', 'o', 'u']
	word = word.lower()
	if word[0] in vowels:
		return word + 'way'
	else:
		return word[1:] + word[0] + 'ay'




if __name__ == '__main__':
	print(pig_latin_converter(raw_input("Enter word: ")))