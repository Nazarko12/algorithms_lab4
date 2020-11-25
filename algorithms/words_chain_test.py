import unittest
from words_chain import read_date_from_csv_file, largest_string_chain


class ChainWordsTest(unittest.TestCase):

    def read_test(self):
        this_date = read_date_from_csv_file()
        self.assertEqual(this_date,
                         ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate',
                          'tea', 'rat', 'a'])

    def test_largest_first_chain(self):
        available_words = ['b', 'bcad', 'bca', 'bad', 'bd']

        self.assertEqual(4, largest_string_chain(available_words))

    def test_largest_second_chain(self):
        available_words = ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate',
                 'tea', 'rat', 'a']

        self.assertEqual(6, largest_string_chain(available_words))

    def test_largest_chain_third(self):
        available_words = ['word', 'another_word', 'yet_another_word']

        self.assertEqual(1, largest_string_chain(available_words))

    def test_largest_chain_fourth(self):
        available_words = ["a", "b", "ba", "bca", "bda", "bdca"]

        self.assertEqual(4, largest_string_chain(available_words))


if __name__ == '__main__':
    unittest.main()
