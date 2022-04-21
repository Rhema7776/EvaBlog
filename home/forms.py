from django.forms import ModelForm
from django import forms
from home.models import Todo,Dev


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['name', 'des']

class DevForm(forms.ModelForm):
    class Meta:
        model = Dev

        fields = ['Describe_yourself', 'location']        