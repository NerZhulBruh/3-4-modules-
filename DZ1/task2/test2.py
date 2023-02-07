import unittest

class TestFile(unittest.TestCase):
    def test_file(self):
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            lines.sort(key=lambda x: int(x.split("-")[1].split(".")[0]))
        with open('output.txt', 'w') as f:
            for line in lines:
                f.write(line)
        with open('output.txt', 'r') as f:
            self.assertEqual(f.read(), "first-1.txt\nsecond-2.txt\nthird-3.txt")

if __name__ == '__main__':
    unittest.main()