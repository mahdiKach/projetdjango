from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Produit,ShippingAdress


class ProduitForm(ModelForm):
	class Meta:
		model = Produit
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ShippingForm(ModelForm):
	class Meta:
		model= ShippingAdress
		fields='__all__'