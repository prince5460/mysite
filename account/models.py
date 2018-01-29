from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE,verbose_name='用户')
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user {}'.format(self.user.username)
