from django.contrib import admin
from accounts.models import UserProfile

class AccountsAdmin(admin.ModelAdmin):
    model = UserProfile
    
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(UserProfile)