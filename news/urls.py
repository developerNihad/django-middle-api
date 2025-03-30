from django.urls import path
from .views import NewsThreeList

urlpatterns = [
    path('', NewsThreeList.as_view(), name='news-json-api'),  # /api/news/
]