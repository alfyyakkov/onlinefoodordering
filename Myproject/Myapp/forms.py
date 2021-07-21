from django import forms

class Signup(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput())
class LogIn(forms.Form):
    email=forms.EmailField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput())
class FileUp(forms.Form):
    Item_name=forms.CharField(max_length=20)
    Item_price=forms.FloatField()
    Item_image=forms.ImageField()
class Billamount(forms.Form):
    Name=forms.CharField(max_length=20)
    Price=forms.FloatField()
    Quatity=forms.IntegerField()