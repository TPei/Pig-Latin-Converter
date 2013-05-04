def pig_latin_converter(word):
	vowels = ['a', 'e', 'i', 'o', 'u']
	word = word.lower()
	pig_word = ''
	counter = 0
	if word[0] in vowels:
		return word + 'way'

	for letter in word:
		if letter in vowels:
			break
		else:
			counter += 1

	pig_word = word[counter:] + word[0: counter] + 'ay'

	return pig_word




if __name__ == '__main__':
	print(pig_latin_converter(raw_input("Enter word: ")))