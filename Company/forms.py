from django import forms
from .models import companyDataset


class companyDatasetForm(forms.ModelForm):
    class Meta:
        model = companyDataset
        fields = '__all__'
