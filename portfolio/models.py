from django.db import models

# Create your models here.

# work was here!!!!!!!!!!


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    name = models.CharField('Name', max_length=255)
    price = models.PositiveIntegerField('Price')
    active = models.BooleanField('Active')
    