import pig_latin
import unittest

class TestPigLatin(unittest.TestCase):
	"""test class for pig_latin.pig_latin_converter. """

	# test words with consonant at the beginning
	def test_with_consonant(self):
		actual = pig_latin.pig_latin_converter("happy")
		expected = "appyhay"
		self.assertEqual(expected, actual)

	def test_with_consonant2(self):
		actual = pig_latin.pig_latin_converter("duck")
		expected = "uckday"
		self.assertEqual(expected, actual)

	# test words with multiple consonants at the beginning
	def test_with_consonants(self):
		actual = pig_latin.pig_latin_converter("flow")
		expected = "owflay"
		self.assertEqual(expected, actual)

	def test_with_consonants2(self):
		actual = pig_latin.pig_latin_converter("fly")
		expected = "flyay"
		self.assertEqual(expected, actual)

	# test words with vowels at the beginning
	def test_with_vowel(self):
		actual = pig_latin.pig_latin_converter("egg")
		expected = "eggway"
		self.assertEqual(expected, actual)

	def test_with_vowel2(self):
		actual = pig_latin.pig_latin_converter("inbox")
		expected = "inboxway"
		self.assertEqual(expected, actual)

	def test_with_sentence(self):
		actual = pig_latin.pig_latin_sentence("what the heck is this stuff")
		expected = "atwhay ethay eckhay isway isthay uffstay "
		self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)