from rest_framework import generics
from .models import NewsThree
from .serializers import NewsThreeSerializer


class NewsThreeList(generics.ListAPIView):

    queryset = NewsThree.objects.all()
    serializer_class = NewsThreeSerializer