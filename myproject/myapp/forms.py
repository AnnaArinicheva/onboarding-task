from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(label='Введите данные', max_length=100)
