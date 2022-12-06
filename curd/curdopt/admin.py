from django.contrib import admin
from .models import asset
from . import models
# Register your models here.
class assetadmin(admin.ModelAdmin):
    pass
admin.site.register(asset, assetadmin)

# class adminlogin1(admin.AdminSite):
#     site_header= 'Admin Login'
#     login_template: 'adminlogin.html'
# blog_site=adminlogin1('adminlogin')
# blog_site.register(models.POST)
