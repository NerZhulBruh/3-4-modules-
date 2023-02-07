import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        with open('input.txt', 'r') as f:
            text = f.read()
        self.assertEqual(text.split(), ['word1', 'word2', 'word3', 'word4'])
    def test_length_of_words(self):
        with open('input.txt', 'r') as f:
            text = f.read()
        for word in text.split():
            self.assertGreater(len(word), 20)
    def test_result_string(self):
        with open('output.txt', 'r') as out:
            result = out.read()
        self.assertEqual(result, 'word1 word2\nword3 word4 ')
        
if __name__ == '__main__':
    unittest.main()