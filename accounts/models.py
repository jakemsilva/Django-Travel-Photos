from django.db import models

from django.contrib.auth.models import Group, User
from registration.signals import user_registered

def get_upload_path(instance, filename):
        import os
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        file_path = '{username}/profile_image/{name}.{ext}'.format(
            username=instance.user.username,name=filename, ext=ext) 
        return file_path
        
def user_registered_callback(sender, user, request, **kwargs):
    g = Group.objects.get(name='tripper') 
    g.user_set.add(user)
 
user_registered.connect(user_registered_callback)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    picture = models.ImageField(upload_to=get_upload_path, blank=True)
    # Override the __unicode__() method to return out something meaningful!
    #def __str__(self):
        #return self.picture
        
