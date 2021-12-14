from django.db import models
import uuid


# Create your models here.
class Users(models.Model):
    userID = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Task(models.Model):
    taskId = models.AutoField(primary_key=True, null=False)
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
