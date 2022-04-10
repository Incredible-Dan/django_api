from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=55)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name = ('article')
            verbose_name_plural = ('articles')

    def __str__(self):
        return self.title