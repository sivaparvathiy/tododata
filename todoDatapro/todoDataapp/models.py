from django.db import models

class todoData(models.Model):
    task_title=models.CharField(max_length=100)
    task_description=models.CharField(max_length=100)
    date=models.DateTimeField()
