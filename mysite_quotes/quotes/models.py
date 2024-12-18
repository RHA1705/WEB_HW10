from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=200)
    born_date = models.CharField(max_length=200)
    born_location = models.CharField(max_length=200)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name

class Quotes(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

