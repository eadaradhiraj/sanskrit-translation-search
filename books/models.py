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


class BiblicalVerse(models.Model):
    verse_title = models.CharField(max_length=20)
    verse_txt = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['verse_title'],
                name='unique_verse'
            )
        ]

    def __str__(self):
        return f"{self.verse_title}"
