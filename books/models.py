import datetime
from django.db import models
from django.utils import timezone

# Create your models here.





class Author(models.Model):
    name = models.CharField(max_length=200)

    birth_date = models.DateTimeField('birthdate')


    def __str__(self):
        return self.name 


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 




class Book(models.Model):
    title = models.CharField(max_length=200)

    num_pages = models.IntegerField(default=0)

    date_published = models.DateTimeField('date published')

    author = models.ForeignKey(Author, null= True, on_delete=models.CASCADE)

    tag = models.ManyToManyField(Tag)

   

      
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title 




