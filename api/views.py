from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from users.models import CustomUser as User
from api.models import Video, VideoCategory, Profile
from .serializers import UserSerializer, ProfileSerializer, VideoSerializer, VideoCategorySerializer
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication


# Create your views here.

# UserAPIView
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@api_view(['PUT', 'DELETE', 'GET'])
def user_detail(request, *args, **kwargs):
    try:
        user = get_object_or_404(User, pk=kwargs['pk'])
    except User.DoesNotExist:
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        user.delete()
        return Response({'details': f'user {kwargs["pk"]} was successfully deleted'}, status=status.HTTP_204_NO_CONTENT)



# ProfileAPIView
@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def profile_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    
@authentication_classes([TokenAuthentication])
@api_view(['PUT', 'DELETE', 'GET'])
def profile_detail(request, *args, **kwargs):
    try:
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
    except Profile.DoesNotExist:
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = request.data
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VideoAPIView
@authentication_classes([TokenAuthentication])
@api_view(['GET', 'POST'])
def video_list(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = VideoSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
@authentication_classes([TokenAuthentication])
@api_view(['PUT', 'DELETE', 'GET'])
def video_detail(request, *args, **kwargs):
    try:
        video = get_object_or_404(Video, pk=kwargs['pk'])
    except Video.DoesNotExist:
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = request.data
        serializer = VideoSerializer(video, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# VideoCategoryAPIView
@authentication_classes([TokenAuthentication])
@api_view(['GET', 'POST'])
def video_category_list(request):
    if request.method == 'GET':
        videos_cat = VideoCategory.objects.all()
        serializer = VideoCategorySerializer(videos_cat, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = VideoCategorySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
@authentication_classes([TokenAuthentication])
def video_category_detail(request, *args, **kwargs):
    try:
        video_cat = get_object_or_404(VideoCategory, pk=kwargs['pk'])
    except Video.DoesNotExist:
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VideoCategorySerializer(video_cat)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = request.data
        serializer = VideoCategorySerializer(video_cat, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        video_cat.delete()
        return Response({"details": "Video was deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    

# Like functionality
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def like_video(request, *args, **kwargs):

    user_id = request.data.get('user_id', None)
    video_id = kwargs['pk']
    
    if video_id is not None and user_id is not None:
        try:
            video = get_object_or_404(Video, pk=int(video_id))
            user = get_object_or_404(User, pk=int(user_id))
            if video.video_like.contains(user):
                video.video_like.remove(user)
                return Response({"detail": f"{user.email} unliked {video.title}"})
            else:
                video.video_like.add(user)
                return Response({"detail": f"{user.email} liked {video.title}"})
        except:
            return Response({"details": "Invalid video_id and user_id"})
    
    return Response({"details": "User Id or Video Id cannot be null"})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def favourite_video(request, *args, **kwargs):

    user_id = request.data.get('user_id', None)
    video_id = kwargs['pk']
    
    if video_id is not None and user_id is not None:
        try:
            video = get_object_or_404(Video, pk=int(video_id))
            user = get_object_or_404(User, pk=int(user_id))
            if video.favourites.contains(user):
                video.favourites.remove(user)
                return Response({"detail": f"{user.email} removed {video.title} from list"})
            else:
                video.favourites.add(user)
                return Response({"detail": f"{user.email} added {video.title} to list"})
        except:
            return Response({"details": "Invalid video_id and user_id"})
    
    return Response({"details": "User Id or Video Id cannot be null"})