from django.db import models

class Blog (models.Model):
    writer = models.TextField(max_length = 100)
    title = models.TextField(max_length = 100)
    subject = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
