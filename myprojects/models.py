from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=60)
    skills=models.TextField()
    profilepic=models.ImageField(upload_to="authorpics")
class myprojects(models.Model):
    title=models.CharField(max_length=60)
    technology=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to="pics")
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    github=models.TextField(max_length=60, null=True)

    def __str__(self):
        return self.title

class comments(models.Model):
    comment_info=models.TextField()
    comment_date=models.DateField(auto_now_add=True)
    myprojects=models.ForeignKey(myprojects,on_delete=models.CASCADE,null=True,blank=True)
    
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    likedprojects=models.ManyToManyField(myprojects)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)        

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return self.user.username





