def pig_latin_converter(word):
	vowels = ['a', 'e', 'i', 'o', 'u']
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	word = word.lower()
	pig_word = ''
	counter = 0
	special_character = ''

	if not (word[-1].lower() in alphabet):
		special_character = word[-1]
		word = word[0:-1]

	if word[0] in vowels:
		return word + 'way'

	for letter in word:
		if letter in vowels:
			break
		else:
			counter += 1

	pig_word = word[counter:] + word[0: counter] + 'ay' + special_character

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