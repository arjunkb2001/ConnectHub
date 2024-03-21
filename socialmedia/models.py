from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

# Create your models here.
class Userprofile(models.Model):
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)
    bio=models.CharField(max_length=200,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    following=models.ManyToManyField(User,related_name="followings",null=True)
    options=(
        ("Male","Male"),("Female","Female"),("Others","Others")
    )
    gender=models.CharField(max_length=200,choices=options,default="Male")
    followers=models.ManyToManyField(User,related_name="followers",null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username



class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_post")
    title=models.CharField(max_length=200)
    post_pic=models.ImageField(upload_to="postpics",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    
    
    def _str_(self):
        return self.title
       


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=400)
    created_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)

class Likes(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="post")
    liked_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")


class Stories(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    storieimg=models.ImageField(upload_to="storieimage")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
def create_userprofile(sender,instance,created, **kwargs):
    
    if created:
        Userprofile.objects.create(user=instance)
post_save.connect(create_userprofile,sender=User)