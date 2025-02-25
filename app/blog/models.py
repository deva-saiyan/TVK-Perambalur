import os
import datetime

from django.db import models

class Register_Model(models.Model):  # Now extending Django's User model
    photo = models.ImageField(upload_to='profile_photos/', blank=False, null=False , default='null')
    name = models.CharField(max_length=20 , unique=False)
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choice, default='M')
    DOB = models.DateField(verbose_name="Date of Birth")
    district = models.CharField(max_length=20, default='Perambalur')
    place = models.CharField(max_length=20, null=False)
    ward_choices = [
        ('1st ward', '1st ward'), ('2nd ward', '2nd ward'), ('3rd ward', '3rd ward'),
        ('4th ward', '4th ward'), ('5th ward', '5th ward'), ('6th ward', '6th ward'),
        ('7th ward', '7th ward'), ('8th ward', '8th ward'), ('9th ward', '9th ward'),
        ('10th ward', '10th ward'), ('11th ward', '11th ward'), ('12th ward', '12th ward'),
    ]
    ward = models.CharField(max_length=10, choices=ward_choices)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=10, verbose_name="Contact Number")
    email = models.EmailField(unique=True)
    id_num = models.CharField(max_length=12, unique=True, verbose_name="ID Number")
    id_photo = models.ImageField(upload_to='id_photos/', blank=False, null=False , default='null')

    def __str__(self):
        return self.name  # Now `username` exists because of AbstractUser



class Slider_Model(models.Model):
    slider1 = models.ImageField(upload_to='slider_photos/', blank=False, null=False)
    slider2 = models.ImageField(upload_to='slider_photos/', blank=False, null=False)
    slider3 = models.ImageField(upload_to='slider_photos/', blank=False, null=False)
    status = models.BooleanField(default=False , help_text='0-show , 1-hidden')
    trending = models.BooleanField(default=False , help_text='0-show , 1-hidden')


  



class Feature_Model(models.Model):
    img1 = models.ImageField(upload_to='feature_photos/', blank=False, null=False)
    img2 = models.ImageField(upload_to='feature_photos/', blank=False, null=False)
    img3 = models.ImageField(upload_to='feature_photos/', blank=False, null=False)
    title = models.CharField(max_length=20)  # Fixed 'tittle' → 'title'
    description = models.CharField(max_length=700)  # Fixed 'nadiscriptionme' → 'description'
    status = models.BooleanField(default=False , help_text='0-show , 1-hidden')
    trending = models.BooleanField(default=False , help_text='0-show , 1-hidden')

    
class Feedback_Model(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10, verbose_name="Contact Number")
    email = models.EmailField(unique=False)
    place = models.CharField(max_length=20, null=False)
    ward_choices = [
        ('1st ward', '1st ward'), ('2nd ward', '2nd ward'), ('3rd ward', '3rd ward'),
        ('4th ward', '4th ward'), ('5th ward', '5th ward'), ('6th ward', '6th ward'),
        ('7th ward', '7th ward'), ('8th ward', '8th ward'), ('9th ward', '9th ward'),
        ('10th ward', '10th ward'), ('11th ward', '11th ward'), ('12th ward', '12th ward'),
    ]
    ward = models.CharField(max_length=10, choices=ward_choices)
    address = models.CharField(max_length=50)
    problem = models.CharField(max_length=700)
    