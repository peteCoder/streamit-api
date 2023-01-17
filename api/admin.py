from django.contrib import admin
from .models import (
    Profile,
    Video,
    VideoCategory
)

# Register your models here.

admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(VideoCategory)
