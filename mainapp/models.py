from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your models here.

class Post(models.Model):
    
    TAGS = (
        ('tech', 'TECH'),
        ('food', 'FOOD'),
        ('spritual', 'SPRITUAL'),
        ('fitness', 'FITNESS'),
        ('motivation', 'MOTIVATION'),
        ('politics', 'POLITICS'),
        ('movies', 'MOVIES'),
        ('music', 'MUSIC'),
    )
    
    post_title= models.CharField(max_length=100)
    post_desc= models.TextField(max_length=2000)
    post_quote= models.TextField(max_length=1000)
    post_image= models.ImageField(null=True, blank=True, upload_to='image/post')
    post_tag= models.CharField(max_length=100, choices=TAGS)
    post_author= models.ForeignKey(User, on_delete=models.CASCADE)
    post_read_min= models.CharField(max_length=50)
    post_date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.post_title


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'post.html', context)