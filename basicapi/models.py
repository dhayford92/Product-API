from django.db import models


class Product(models.Model):
    item = models.CharField(max_length = 100)
    price = models.FloatField()
    qantity = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
