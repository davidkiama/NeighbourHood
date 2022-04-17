from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    neighbourhood = models.ForeignKey(
        'Neighbourhood', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()


class Neighbourhood(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.location}'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.save()

    def update_occupants_count(self):
        self.occupants_count += 1
        self.save()

    @classmethod
    def find_neighbourhood_by_id(cls, id):
        return cls.objects.get(id=id)
