from django.db import models

class Products(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Product'

