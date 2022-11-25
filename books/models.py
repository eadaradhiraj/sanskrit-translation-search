from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=10)
    book = models.TextField()

    def __str__(self):
        return self.name

    # class Meta:
    #     indexes = [
    #         GinIndex(fields=["book"]),
    #     ]
