from django.db import models

class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryName