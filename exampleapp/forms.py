from django import forms


class TextForm(forms.Form):
    sum_form = forms.CharField(widget=forms.Textarea(attrs={'class': "sum-form"}), label="")