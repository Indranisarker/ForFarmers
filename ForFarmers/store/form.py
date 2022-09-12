from django import forms
from .models import Order, Customer
from django.contrib.auth.models import User


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
                  "mobile", "email","payment_method"]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]

        def clean_username(self):
            uname = self.cleaned_data.get("username")
            if User.objects.filter(username=uname).exists():
                raise forms.ValidationError(
                    "Customer with this username already exists.")

            return uname


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter the email used in customer account..."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with this account does not exists..")
        return e
