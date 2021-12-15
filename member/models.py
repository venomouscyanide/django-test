from django.db import models
from django.urls import reverse

# Create your models here
class Member(models.Model):
    first_name = models.CharField(max_length=3)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length = 200)
    role = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('member_detail', args=[str(self.id)])
