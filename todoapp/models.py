from django.db import models

# Create your models here.


class Todo(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    textarea = models.TextField(max_length=250)

    def __str__(self):
        return (self.first_name + " " + self.last_name)
