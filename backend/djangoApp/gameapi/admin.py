from django.contrib import admin
from .models import Game

# This line registers the Game model with the admin site so the admin user
# can add and change data via the admin site
admin.site.register(Game)
