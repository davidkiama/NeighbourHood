from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(
        'Neighbourhood', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()


# Create your models here.
