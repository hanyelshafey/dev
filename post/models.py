from django.db import models
from django.utils import timezone

# Create your models here.

class Post (models.Model):

    title=models.CharField(max_length=50)
    content=models.TextField(max_length=500)
    imag=models.ImageField(null = True ,upload_to = 'posts/')
    publish=models.DateTimeField(default=timezone.now)
    views=models.IntegerField(default=0)



    



    def __str__(self):
        return self.title

    class Meta:
        ordering=[('-id')        ]
        verbose_name='post'
        verbose_name_plural='posts'