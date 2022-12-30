from django import forms
from coco1.models import ProfileData

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileData
        fields = '__all__'


class StudentForm(forms.Form):
    firstname = forms.CharField(label="enter first name",max_length=100)
    lastname = forms.CharField(label="enter last name",max_length=100)
    email = forms.EmailField(label="enter email id",max_length=25)
    age = forms.IntegerField()


