from rest_framework import serializers
from users.models import CustomUser as User
from .models import Profile, Video, VideoCategory

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields =  ['id', 'title', 'thumbnail', 'author_', '_category', 'date_uploaded', 'last_modified']

        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'email', 
            'is_superuser', 
            'is_active', 
            'date_joined',
            'last_login'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    author = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'



class VideoCategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = VideoCategory
        fields = '__all__' # ['name', 'videos'] 
