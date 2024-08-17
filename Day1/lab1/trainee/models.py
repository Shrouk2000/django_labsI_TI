from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    progress = models.TextField()

    def __str__(self):
        return self.name