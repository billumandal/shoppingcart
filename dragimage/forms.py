from django import forms
from models import UploadFile, Picture, FourthTry

class PhotoUploadForm(forms.Form):
    # Keep name to 'file' because that's what Dropzone is using
    file = forms.ImageField(required=True)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ('user_image1', 'user_image2', 'user_image3', 'user_image4', 'user_image5')

class FourthTryForm(forms.ModelForm):
    class Meta:
        model = FourthTry
        fields = ('picture_name', 'picture')
