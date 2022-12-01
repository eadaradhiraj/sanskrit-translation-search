from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, BiblicalVerse
import re


class BiblicalVerseList(LoginRequiredMixin, ListView):
    model = BiblicalVerse
    context_object_name = "verses"
    template_name = "verse.html"

    def get_queryset(self):

        return BiblicalVerse.objects.filter(
                verse_title__istartswith=self.request.GET.get("q")
        ).order_by('verse_title').values()


class SearchResultsList(LoginRequiredMixin, ListView):
    """
    Retrieve search results based on regex search
    """

    model = Book
    context_object_name = "sents"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        sents = []
        regexp = re.compile(query)
        for book in Book.objects.filter(book__regex=query):
            for sent in book.book.split("\r\n\r\n"):
                sent_split = sent.split("\r\n")
                if (len(sent_split) == 2) and (
                    regexp.search(sent_split[0]) or
                    regexp.search(sent_split[1])
                ):
                    sents.append(sent_split)
        return sents
