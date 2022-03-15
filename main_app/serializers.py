from multiprocessing import Event
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User, Player, Game, Event

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = Player
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write-only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class GameSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    crossplay = serializers.BooleanField()
    img = serializers.ImageField()
    
    class Meta:
        model = Game
        fields = ('name', 'crossplay', 'img')
        
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('game', 'name', 'players', 'description', 'location', 'creator', 'spotsAvailable', 'spotsTotal')
        
    
        