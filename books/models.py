from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.views import get_user_model


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['last_name']


class Book(models.Model):
    STATUS_CHOICES = [
        ('pub', 'published'),
        ('drf', 'draft')
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    text = models.TextField()
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    # cover =

    # datetime_created = models.DateTimeField(auto_now_add=True)
    # datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'




