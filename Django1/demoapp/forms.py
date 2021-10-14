from django import forms
from .models import Users

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20)
    age = forms.IntegerField(label='Age')
    address = forms.CharField(label='Address', max_length=100, widget=forms.Textarea(attrs={'rows':2, 'cols':23}))

    def save(self):
        user = Users.objects.create(name=self.cleaned_data['name'], age=self.cleaned_data['age'], address=self.cleaned_data['address'])
        user.save()