from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column')
    column = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

