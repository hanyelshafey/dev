from django.db import models

# Create your models here.
class Profile (models.Model):

    name=models.CharField(max_length=50)
    imag=models.ImageField(null = True ,upload_to = 'posts/')
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering=[('-id')        ]
        verbose_name='post'
        verbose_name_plural='posts'