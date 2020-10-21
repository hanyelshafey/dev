from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imag=models.ImageField(null = True ,upload_to = 'posts/',  blank= True)
    phon=models.CharField(max_length=100 , null=True , blank= True)

    def __str__(self):
        return self.user

    class Meta:
        ordering=[('-id')        ]
        verbose_name='Profile'
        verbose_name_plural='Profiles'


print('1')
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

print('2')