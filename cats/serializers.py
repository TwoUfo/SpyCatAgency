from typing import Any

from rest_framework.serializers import ModelSerializer, ValidationError

from cats.models import Cat


class CatListCreateSerializer(ModelSerializer[Cat]):
    class Meta:
        model = Cat
        fields = ("id", "name", "expirience", "salary", "breed")


class CatRetrieveUpdateDestroySerializer(ModelSerializer[Cat]):
    class Meta:
        model = Cat
        fields = ("id", "name", "expirience", "salary", "breed")