from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} --- {self.description[:50]}'

class Comment(models.Model):
    body = models.CharField(max_length=100)
    category = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.body