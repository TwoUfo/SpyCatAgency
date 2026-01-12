from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cats.models import Cat
from cats.serializers import CatListCreateSerializer, CatRetrieveUpdateDestroySerializer

class CatListCreateView(ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatListCreateSerializer
    name = "Cat list create"


class CatRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatRetrieveUpdateDestroySerializer
    name = "Cat list update destroy"
    lookup_field = "id"

