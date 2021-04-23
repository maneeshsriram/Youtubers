from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Youtuber(models.Model):

    crew_choices = (
        ('single', 'solo'),
        ('small', 'duo'),
        ('large', 'team'),
    )

    camera_choices = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('red', 'red'),
        ('fugy', 'fugy'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    )

    category_choices = (
        ('code', 'code'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('gaming', 'gaming'),
        ('other', 'other')
    )

    name = models.CharField(max_length=75)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=500)
    description = RichTextField()  # ckeditor
    city = models.CharField(max_length=75)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(max_length=100, choices=crew_choices)
    camera = models.CharField(max_length=100, choices=camera_choices)
    subs_count = models.IntegerField()
    category = models.CharField(max_length=100, choices=category_choices)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
