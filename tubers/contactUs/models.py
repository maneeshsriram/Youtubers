from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.full_name
