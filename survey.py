# coding:utf8

class AnonymousSurvey():

    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('Survey results:')
        for response in self.responses:
            print('-' + response)
#my_survey = AnonymousSurvey('What language did you first learn to speak?')
#my_survey.show_question()
#while True:
#    response = input('language: ')
#    if response == 'q':
#        break
#    my_survey.store_response(response)
#my_survey.show_results()
