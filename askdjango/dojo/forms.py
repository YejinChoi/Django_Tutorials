#dojo/forms.py
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.') #예외만 발생하는 형태

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator]) # 함수 넘겨줄 때 min_length_3_validator()로 넘겨주는 것이 아님!
    content = forms.CharField(widget=forms.Textarea)
    # 현재는 값이 있는지만 검사