from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import User, Business, YelpInputModel, Googlemodel, GoogleInputmodel, NutritionInputmodel, Nutritionmodel, Foodnutritionmodel, FoodnutritionInputmodel


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class YelpForm(forms.ModelForm):
    term = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'term'}))
    location = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'location'}))

    class Meta:
        model = YelpInputModel
        fields = ("term", "location")        

class BusinessForm(forms.Form):
    alias = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'alias'}))
    display_phone = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'display_phone'}))
    address1 = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'address1'}))
    address2 = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'address2'}))

    class Meta:
        model = Business
        fields = ("alias", "display_phone", "address1", "address2")
        
    def save(self, commit=True):
        business = super(BusinessForm, self).save(commit=False)
        business.alias = self.cleaned_data['alias']
        business.display_phone = self.cleaned_data['display_phone']
        business.address1 = self.cleaned_data['address1']
        business.address2 = self.cleaned_data['address2']
        if commit:
            business.save()
            return business

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         #model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # not USERNAME_FIELD = username
    USERNAME_FIELD = 'username'
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            return user

class GoogleForm(forms.ModelForm):
    Foodinput = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'Foodinput'}))
    
    class Meta:
        model = GoogleInputmodel
        fields = ("Foodinput",) 

class NutritionForm(forms.ModelForm):
    Nutritioninput = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'Nutritioninput'}))
    
    class Meta:
        model = NutritionInputmodel
        fields = ("Nutritioninput",) 

class FoodNutrientsForm(forms.ModelForm):
    Macroinput = forms.CharField(max_length=254, widget=forms.TextInput({'class': 'form-control',
                                   'placeholder': 'Macroinput'}))
    
    class Meta:
        model = NutritionInputmodel
        fields = ("Macroinput",) 