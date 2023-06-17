from django import forms

class IsiRapat(forms.Form):
    desc_rapat = forms.CharField(widget=forms.Textarea, label="Isi Rapat", required=True)