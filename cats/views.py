from rest_framework.generics import ListCreateAPIView

from cats.models import Cat
from cats.serializers import CatListCreateSerializer

class CatListCreateView(ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatListCreateSerializer
    name = "Cat list create"
