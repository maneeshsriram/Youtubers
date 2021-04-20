from django.db import models

# Create your models here.


class Slider(models.Model):
    headline = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    link = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=75)
    fb_link = models.CharField(max_length=250)
    insta_link = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class aboutData(models.Model):
    description = models.TextField()

    def __str__(self):
        return str(self.description)


class HeaderData(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
