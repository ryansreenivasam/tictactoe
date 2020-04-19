from rest_framework import serializers
from .models import Game

# This class will tell the REST framework how to serialize the Game model.
class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'board',)
