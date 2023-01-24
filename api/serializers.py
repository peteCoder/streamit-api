from rest_framework import serializers
from users.models import CustomUser as User
from .models import Profile, Video, VideoCategory

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields =  ['id', 'title', 'thumbnail', 'author_', 'video_file', '_category', 'likes', 'date_uploaded', 'last_modified']

        
class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'email', 
            'is_superuser', 
            'is_active', 
            'date_joined',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                
            },
            'password2': {
                'write_only': True,
                
            }
        }
        
    def save(self):
        user = User(email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        else:
            user.set_password(password)
            user.save()
            return user


class ProfileSerializer(serializers.ModelSerializer):
    videos_uploaded = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['user_details', 'username', 'first_name', 'last_name', 'profile_photo', 'bio', 'videos_uploaded', 'country', 'gender', 'phone_number']



class VideoCategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = VideoCategory
        fields = '__all__' # ['name', 'videos'] 
