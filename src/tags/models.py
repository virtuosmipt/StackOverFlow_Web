from django.db import models


class Tags(models.Model):
    tags_name = models.CharField(max_length=100)

# Create your models here.
