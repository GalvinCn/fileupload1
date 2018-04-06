from django.db import models

# Create your models here.

class Contributor(models.Model):
    author_id = models.CharField(max_length=10)
    author_name = models.CharField(max_length=50)
    post_total = models.IntegerField(default=0)
    views_total = models.IntegerField(default=0)


class Post(models.Model):
    post_id = models.IntegerField(default=0)
    post_title = models.CharField(max_length=200)
    post_file_url = models.CharField(max_length=200)
    post_description = models.CharField(max_length=5000)
    upload_date = models.DateTimeField('upload date')
    down_total = models.IntegerField(default=0)







