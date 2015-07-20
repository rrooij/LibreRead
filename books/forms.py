from django.forms import ModelForm

from .models import BookReader, User


class UserForm(ModelForm):
    class Meta:
        model = User


class BookReader(ModelForm):
    class Meta:
        model = BookReader
        excluse = ['user']
