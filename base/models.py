from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #Cascade deletes tasks when the user is deleted
    title = models.CharField(max_length=200,)
    description = models.TextField(null=True, blank=True) #empty field
    complete = models.BooleanField(default=False) #task starts as not-completed
    created = models.DateTimeField(auto_now_add=True) #automatically assigns the date and time

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete'] #orders incomplete and complete tasks together