# Author: Ryan Sreenivasam
# Description: Describes what data the admin user has access to from the admin 
# site. 
# Admin site is here http://127.0.0.1:8000/admin/gameapi/game/ 
# Username: admin
# Password: 123456

from django.contrib import admin
from .models import Game

# This line registers the Game model with the admin site so the admin user
# can add and change data via the admin site.
admin.site.register(Game)
