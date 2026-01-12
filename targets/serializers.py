from rest_framework.serializers import ModelSerializer

from targets.models import Target


class TargetListCreateSerializer(ModelSerializer[Target]):
    class Meta:
        model = Target
        fields = ("id", "name", "notes", "country")


class TargetRetrieveUpdateSerializer(ModelSerializer[Target]):
    class Meta:
        model = Target
        fields = ("id", "name", "notes", "country", "completed")
