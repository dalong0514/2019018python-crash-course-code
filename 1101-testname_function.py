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
    def setUp(self):
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
    
if __name__ == '__main__':
    unittest.main()