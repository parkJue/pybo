from django import forms
from pybo.models import Question, Answer

# Question 모델과 연결된 폼이고, 속성으로 Question 모델의 subject와 content를 사용한다고 정의한 것 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject','content'] # QuestionForm에서 사용할 Question 모델의 속성
        
        # # 부트스트랩 사용을 위함
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        # Subject -> '제목', Content -> '내용'
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }