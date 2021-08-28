from django.db import models


class Logs(models.Model):
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    method = models.CharField(max_length=200)

    def __str__(self):
        return self.path
