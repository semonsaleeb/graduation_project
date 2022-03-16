from django import forms
from django.forms import ModelForm
from .models import Cgr


class CgrForm(ModelForm):
    class Meta:
        model = Cgr
        fields = ['id','upload_file', 'type_of_file', 'kmer_size']


# class ImgForm(ModelForm):
#     class Meta:
#         model = Img
#         fields = ('id', 'img')



