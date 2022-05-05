from statistics import mode
from django.db import models

# Create your models here.
# Many to one

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline