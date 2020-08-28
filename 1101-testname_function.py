import unittest

def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_upper(self):
        formatted_name = get_formatted_name('feng', 'long')
        self.assertEqual(formatted_name, 'Feng Long')

if __name__ == '__main__':
    unittest.main()