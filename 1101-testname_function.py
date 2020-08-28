import unittest

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_frist_last_name(self):
        formatted_name = get_formatted_name('feng', 'long')
        self.assertEqual(formatted_name, 'Feng Long')
    
    def test_frist_last_middle_name(self):
        formattted_name = get_formatted_name('feng', 'long', 'da')
        self.assertEqual(formattted_name, 'Feng Da Long')

if __name__ == '__main__':
    unittest.main()