from django.db import models

class Books(models.Model):
    name = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    # writer = models.CharField(max_length = 100)

    def __str__(self):
        return self.name