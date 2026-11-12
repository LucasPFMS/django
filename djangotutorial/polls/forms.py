from django import forms
class QuestionAddForm(forms.Form):
    question_text = forms.CharField(label='Question text')
    choice_0 = forms.CharField(label='choice #1')
    choice_1 = forms.CharField(label='choice #2', required=False)
    choice_2 = forms.CharField(label='choice #3', required=False)
    choice_3 = forms.CharField(label='choice #4', required=False)
    choice_4 = forms.CharField(label='choice #5', required=False)