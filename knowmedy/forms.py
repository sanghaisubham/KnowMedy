from django import forms

class MainForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'class':'form-control','placeholder':'Enter the name please!'}
                           ))

class Sympform(forms.Form):
    symptoms1 = forms.CharField(max_length=128,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control mt-2', 'placeholder': 'Enter the symptom'}
                                ))
    severity1 = forms.IntegerField(min_value=1, max_value=5,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control mt-1', 'placeholder': 'Enter the severity'}
                                   ))
    symptoms2 = forms.CharField(max_length=128,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control mt-2', 'placeholder': 'Enter the symptom'}
                                ))
    severity2 = forms.IntegerField(min_value=1, max_value=5,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control mt-1', 'placeholder': 'Enter the severity'}
                                   ))
    symptoms3 = forms.CharField(max_length=128,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control mt-2', 'placeholder': 'Enter the symptom'}
                                ))
    severity3 = forms.IntegerField(min_value=1, max_value=5,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control mt-1', 'placeholder': 'Enter the severity'}
                                   ))