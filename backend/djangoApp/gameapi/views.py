# Author: Ryan Sreenivasam
# Description: The views take all relevant data from the database and present 
# it to the proper serializer for conversion.

from django.shortcuts import render
from .models import Game
from .serializers import GameSerializer
from rest_framework import viewsets

# This class will use the serializer to render data for a game object into JSON
# format. The queryset will query the database for all game objects then pass 
# that data to the serializer where it is converted to JSON.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
