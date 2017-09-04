# coding:utf8

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):

        """创建一个调查对象和一组答案，供使用的测试方法使用"""

        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['enlish','chinese']

    def test_store_single_response(self):
#        my_survey = AnonymousSurvey('What language did you first learn to speak?')
#        responses = ['english','chinese','minnanyu']
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_two_response(self):

        """测试两个答案会被妥善地储存"""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
