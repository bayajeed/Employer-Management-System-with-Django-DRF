from django.db import models

# Create your models here.

class NewsPost(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'news/', blank=True, null=True)

    def __str__(self):
        return self.title