from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser as User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    profile_photo = models.ImageField(
        blank=True,
        null=False,
        upload_to='media/profile/'
    )
    bio = models.TextField(
        help_text="Enter not more than 200 words.. ",
        max_length=200,
        verbose_name="User bio"
    )

    def __str__(self):
        return self.first_name + " | " + self.user.email


class VideoCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, related_name='videos')
    thumbnail = models.ImageField(
        blank=True,
        null=False,
        upload_to='media/video/'
    )
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    @property
    def _category(self):
        category = {
            'id': self.category.id,
            'name': self.category.name
        }
        
        return category
    
    @property
    def author_(self):
        author = {
            'id': self.author.user.id,
            'first_name': self.author.first_name,
            'last_name': self.author.last_name
        }
        return author

    def __str__(self):
        return self.author.email


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
