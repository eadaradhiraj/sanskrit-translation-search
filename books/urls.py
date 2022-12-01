from django.urls import path

from .views import SearchResultsList, BiblicalVerseList

urlpatterns = [
    path("search/", SearchResultsList.as_view(), name="search_results"),
    path("verse/", BiblicalVerseList.as_view(), name="verse_results"),
]
