from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class To_Do_List(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.Title