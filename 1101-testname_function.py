import unittest

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('feng', 'long')
        self.assertEqual(formatted_name, 'Feng Long')
    
    def test_first_last_middle_name(self):
        formattted_name = get_formatted_name('feng', 'long', 'da')
        self.assertEqual(formattted_name, 'Feng Da Long')

class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print('Survey results: ')
        for response in self.responses:
            print('- ' + response)

class AnonymousSurveyTestCase(unittest.TestCase):
    def test_store_single_response(self):
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
if __name__ == '__main__':
    unittest.main()