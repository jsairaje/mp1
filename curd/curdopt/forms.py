from django import forms
from .models import asset
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
class assetfoem(forms.ModelForm):
    Image=forms.ImageField(label='Asset_image', required=True)
    sr_no = forms.IntegerField()
    class Meta:
        model=asset  
        fields="__all__"
        widgets={
            # 'Date':forms.number(attrs={'class':'form-control'}),
            # 'Date':forms.DateTimeField(attrs={'class':'form-control'}),
            # 'Date_of_verification':forms.DateField(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'vr_no':forms.TextInput(attrs={'class':'form-control'}),
            'Date':forms.DateInput(attrs={'type': 'date'}),
            'make':forms.TextInput(attrs={'class':'form-control'}),
            'identification_mark':forms.TextInput(attrs={'class':'form-control'}),
            'Name_of_the_party_from_whome_purchesed':forms.TextInput(attrs={'class':'form-control'}),
            'funds':forms.TextInput(attrs={'class':'form-control'}),
            'Varified_by':forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_verification':forms.DateInput(attrs={'type': 'date'}),
            'Remark':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ImageField(label='Asset_image', required=False),
            'Laboratory':forms.TextInput(attrs={'class':'form-control'}),
        }
    def merge_from_initial(self):
        filt = lambda v: v not in self.data.keys()
        for field in filter(filt, getattr(self.Meta, 'fields', ())):
            self.data[field] = self.initial.get(field, None)

class AdminSigupForm(forms.ModelForm):
    email = forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['email','username','password1','password1']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.TextInput(attrs={'class':'form-control'}),
        }



# class StudentUserForm(forms.ModelForm):
#     email = forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
#     username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
#     password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model=User
#         fields=['email','username','password1','password2']


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",
                               max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    
    email = forms.EmailField(label="",
                             max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="",
                                max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", 
                                max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 
                  'email', 'password1', 'password2']
        labels={'email':'Email'}
        