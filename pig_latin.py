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


def pig_latin_sentence(sentence):
	words = sentence.split()
	pig_latin = ''
	for word in words:
		word = pig_latin_converter(word)
		pig_latin += word + ' '

	return pig_latin



if __name__ == '__main__':
	print(pig_latin_sentence(raw_input("Enter a sentence: ")))