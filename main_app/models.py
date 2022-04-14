from django.db import models
from django.urls import reverse 

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('galleries_detail', kwargs={'pk': self.id})

class Art(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'a_id': self.id})


class Comment(models.Model):
    title = models.TextField(
        max_length=100,
        default='Add Title'
    )
    text = models.TextField(
        max_length=300,
        default='Type Here'
    )

    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
