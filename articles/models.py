from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model




class Section(models.Model):
    description=models.TextField()
    name=models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Article(models.Model):
    article=models.CharField(max_length=255)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    author=models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,  
        null=True,
        blank=True,
        default=None

    )
    
    section=models.ForeignKey(
        Section,
        on_delete=models.CASCADE,  
        null=True,
        blank=True,
        default=None
    )


    def __str__(self):
        return self.author
    
    def get_absolute_url(self):
        return reverse('article_detail',args=[self.id])
