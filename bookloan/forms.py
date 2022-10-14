
from django import forms
from .models import Bookloan


class BookloanForm(forms.ModelForm):
    class Meta:
        model = Bookloan
        fields =['bookloan_note']
