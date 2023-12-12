from django.db import models
from categories.models import CategoryModel
from django.contrib.auth.models import User

class PostModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskTitle