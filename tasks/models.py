from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, default=' ')
    slug = models.SlugField(max_length=100)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    comple_before = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.name
