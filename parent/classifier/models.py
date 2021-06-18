from django.db import models

# Create your models here.
class Image(models.Model):
    LAND_COVERAGE = (
        ('Fo', 'Forest'),
        ('Mo', 'Mountain'),
        ('Ur', 'Urban'),
    )


    #variables for image data 
    name = models.TextField(max_length=200)
    url = models.URLField(blank=True)
    data = models.ImageField()
    category = models.CharField(max_length=2, choices=LAND_COVERAGE)

    def __str__(self):
        return self.name

