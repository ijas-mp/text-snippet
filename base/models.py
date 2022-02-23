from pyexpat import model
from sqlite3 import Timestamp
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tagdetails(models.Model):
    tag_title = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.tag_title

class textdetails(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User,on_delete=models.CASCADE)
    textdata = models.CharField(max_length=500, blank=True, null=True)
    tag_id = models.ForeignKey(tagdetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

