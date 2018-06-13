from django.db import models

# Create your models here.
class MainModel(models.Model):
    name = models.CharField(max_length=100)
    introduction  = models.TextField(default="")
    causes = models.TextField(default="")
    symptoms = models.TextField(blank="")
    diagnosis = models.TextField(blank="")
    complications = models.TextField(blank="")
    medicine = models.TextField(blank="")
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.name
