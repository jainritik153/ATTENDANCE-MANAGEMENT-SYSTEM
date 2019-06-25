from django import forms
from student.models import *


class StudentReg(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
        widget=forms.EmailInput()
    )

    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
    roll= forms.IntegerField(required=True)

    class Meta:
        model = Studentreg
        fields = ('username', 'email', 'password', 'roll')




class TeacherReg(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )

    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
    subject = forms.CharField(
        required=True,
        label='subject',
        max_length=32,
    )

    class Meta:
        model = Teacherreg
        fields = ('username', 'email','password','subject')