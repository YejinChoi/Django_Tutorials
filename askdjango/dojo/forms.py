#dojo/forms.py
from django import forms
from .models import Post

#validator는 dojo/models.py에 정의
#def min_length_3_validator(value):
    #if len(value) < 3:
        #raise forms.ValidationError('3글자 이상 입력해주세요.') #예외만 발생하는 형태


#어던 모델의 어떤 필드로 어떤 폼을 만들겠다 정의
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
        #전체 필드
        #fields = '__all__'
        widget = {
            'user_agent' : forms.HiddenInput,
        }

'''
class PostForm(forms.Form):

    title = forms.CharField(validators=[min_length_3_validator]) # 함수 넘겨줄 때 min_length_3_validator()로 넘겨주는 것이 아님!
    content = forms.CharField(widget=forms.Textarea)
    # 현재는 값이 있는지만 검사


    #Models.save 인터페이스를 흉내내어 구현
    #commit이 저장 유무를 결정
    def save(self, commit=True): #commit이 ture == model.instance 의 save() 호출
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
    '''
