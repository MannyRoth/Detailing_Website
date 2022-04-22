from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length= 100)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length= 300)

    def __str__(self):
        return self.email
