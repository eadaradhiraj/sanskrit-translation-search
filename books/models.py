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
    book = models.CharField(max_length=20)
    verse_txt = models.TextField()
    chapter = models.IntegerField()
    verse_num = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'chapter', 'verse_num'],
                name='unique_verse'
            )
        ]

    def __str__(self):
        return f"{self.book} {self.chapter}:{self.verse_num}"

