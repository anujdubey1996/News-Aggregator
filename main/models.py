from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    icon=models.CharField(max_length=500)
    title=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title


class News(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    article_image=models.ImageField(upload_to='imgs/')
    details=models.TextField()
    likes=models.BigIntegerField(default=0)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

class Like(models.Model):
    id= models.BigIntegerField(primary_key=True)
    user = models.CharField(max_length=50,default='anuj04')
    article_id = models.CharField(max_length=300) 
    
    class Meta:
        verbose_name_plural = "Likes"
    
    def __str__(self):
        return self.user      
