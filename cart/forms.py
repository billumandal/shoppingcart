from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.core import validators
from cart.models import Product, UserProfile

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		exclude = ('sellerid',)

	# productname = forms.CharField(label="Name of the Product", max_length=255, widget=forms.TextInput,)
	# price = forms.IntegerField(label="Price of the item: Rs. ")
	# selling_starts_on = forms.DateField(label="Selling Starts On ", widget=AdminDateWidget)
	# selling_ends_on = forms.DateField(label="Selling Ends On ", widget=AdminDateWidget)
	# despatched_from = forms.CharField(label="Item despatched from ", max_length=30)
	# image = forms.ImageField(label="Optionally add an Image of the Product")

	error_css_class = 'error'
	required_css_clss = 'required'

class RegistrationForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur','class':'form-control input-perso'}),max_length=30,min_length=3,validators=[validators.validate_slug])
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control input-perso'}),max_length=100,error_messages={'invalid': ("Email invalid.")},validators=[validators.validate_email])
    password1 = forms.CharField(label="",max_length=50,min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe','class':'form-control input-perso'}))
    password2 = forms.CharField(label="",max_length=50,min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer mot de passe','class':'form-control input-perso'}))

    #recaptcha = ReCaptchaField()

    #Override of clean method for password check
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            self._errors['password2'] = ErrorList([u"Le mot de passe ne correspond pas."])

        return self.cleaned_data

    #Override of save method for saving both User and Profil objects
    def save(self, datas):
        u = User.objects.create_user(datas['username'],
                                     datas['email'],
                                     datas['password1'])
        u.is_active = False
        u.save()
        profil=Profil()
        profil.user=u
        profil.activation_key=datas['activation_key']
        profil.key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        profil.save()
        return u

    #Handling of activation email sending ------>>>!! Warning : Domain name is hardcoded below !!<<<------
    #I am using a text file to write the email (I write my email in the text file with templatetags and then populate it with the method below)
    def sendEmail(self, datas):
        link="http://yourdomain.com/activate/"+datas['activation_key']
        c=Context({'activation_link':link,'username':datas['username']})
        f = open(MEDIA_ROOT+datas['email_path'], 'r')
        t = Template(f.read())
        f.close()
        message=t.render(c)
        #print unicode(message).encode('utf8')
        send_mail(datas['email_subject'], message, 'yourdomain <no-reply@yourdomain.com>', [datas['email']], fail_silently=False)
