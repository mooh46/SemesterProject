from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

#userAdmin manages user accounts in admin panel tells django how user information should be displayed, created and edited in the panel
#User not an ordinary model, it has special fields and behaviours particularly when it comes to passwords and permissions
# django should hash passwords before storing them
#allows us to edit user details on the details on the admin panel a
admin.site.register(User, UserAdmin)
admin.site.register(Post)


#so how hashing works when a user creates a password django hashes it so it unrecognizable so when the user log in with that password django hashes that one to and looks for the one that matches it

# Register your models here.

