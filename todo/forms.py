from django import forms

class TodoForm(forms.Form):
	task=forms.CharField(max_length=20,
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'A Django TODO'

			}))