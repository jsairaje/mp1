from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
import os
# class User(AbstractUser):
#     isuser = models.BooleanField(default=False)
#     isadmin = models.BooleanField(default=False)

# class admininfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=12)
    

#     def __str__(self):
#         return self.user.username

# class userinfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=12)
    
    

#     def __str__(self):
#         return self.user.username


# def filepath(request ,filename):
#     old_filename=filename
#     # timenow=datetime.now().strftime("%y%m%d%H%M%S")
#     filename="%s%s",(old_filename)
#     return os.path.join('/media/' ,filename)


# Overriding the Default Django Auth User and adding One More Field (user_type)
# class CustomUserCustomUser(AbstractUser):
#     user_type_data = ((1, "HOD"), (2, "Staff"),(3,"apiView"))
#     user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

# class AdminHOD(models.Model):
#     id = models.AutoField(primary_key=True)
#     # admin = models.(on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()


# class Staffs(models.Model):
#     id = models.AutoField(primary_key=True)
#     # admin = models.OneToOneField(on_delete = models.CASCADE)
#     address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

class asset(models.Model):
   
    sr_no = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100 ,null=True)
    vr_no = models.CharField(max_length=100 ,null=True)
    Date= models.DateField(  null=True)  
    make = models.CharField(max_length=30 ,null=True)
    identification_mark = models.CharField(max_length=30 ,null=True)
    Name_of_the_party_from_whome_purchesed = models.CharField(max_length=30 ,null=True)
    value=models.FloatField(null=True)
    funds = models.CharField(max_length=30 ,null=True)
    Dept_stock_register_folio_number = models.PositiveIntegerField(null=True)
    Varified_by = models.CharField(max_length=30 ,null=True)
    Date_of_verification = models.DateField(null=True)
    Remark=models.CharField(max_length=100 ,null=True )
    Image=models.ImageField(upload_to="media" ,null=True ,blank=True ,default='default.jpg')
    # Image=models.FileField(max_length=250 ,null=True ,default=None)
    Laboratory=models.CharField(max_length=100 ,null=True)
    
    def save(self):
        super().save()
        img = Image.open(self.Image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Image.path)

    def __str__(self):
        return str(self.sr_no)

    class meta:
        db_table='asset'

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
#     def __str__(self):
#         return f"{self.user.username}'s profile"


# Create your models here.





