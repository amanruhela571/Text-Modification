from django.db import models
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
# from django import PhoneField
# from phonenumber_field.modelfields import PhoneNumberField
# from django.utils.translation import gettext_lazy as _

# from phone_field import PhoneField

# Create your models here.

class Regular_user(models.Model):                                   # models for regular user

     id=models.AutoField
     email=forms.EmailField(label=('entre your email'))
     phone_number=models.IntegerField(blank=True,help_text='Contact phone number')
     # phone_number=models.IntegerField(max_length=12)
     school=models.CharField(max_length=30)
     # date_of_birth = models.DateField(verbose_name=_("Date of birth"), blank=True, null=True)     
     github=models.CharField(max_length=30)
     active_coding_platfor=models.CharField(max_length=20)

# class YourForm(forms.ModelForm):
     from_date = forms.DateField(widget=AdminDateWidget())



     # phone_number = PhoneField(blank=True, help_text='Contact phone number')





     # from_date = forms.DateField(widget=AdminDateWidget())
     # date = models.DateField(forms.Widget(AdminDateWidget()), null=True)
