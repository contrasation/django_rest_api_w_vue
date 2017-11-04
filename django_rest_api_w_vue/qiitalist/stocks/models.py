from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Stock(models.Model):

    class Meta:
        db_table = "stock"
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    stock_count = models.IntegerField()
