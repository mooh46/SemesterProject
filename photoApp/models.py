from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    #django only stores the path to images in the database so i must create a folder in my project where the images will be stored
    # pillow library installed to help process photos, image field relies on pillow to process images
    # configured MEDIA_ROOT to BASE_DIR/ = 'media/' this tells django where the folder that stores the photos is located
    #MEDIA_URL = /media/ tells django the URL prefix that can be used to acces the images
    picture = models.ImageField(upload_to='user_posts/')
    caption = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)