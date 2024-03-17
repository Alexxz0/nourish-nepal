from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser, Food

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'address',)

class LoginForm(AuthenticationForm):
    pass

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['picture', 'name', 'description', 'price', 'calories', 'protein']