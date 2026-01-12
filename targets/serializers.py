from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from targets.models import Target


class TargetListCreateSerializer(ModelSerializer[Target]):
    class Meta:
        model = Target
        fields = ("id", "name", "notes", "country")


class TargetRetrieveUpdateSerializer(ModelSerializer[Target]):
    class Meta:
        model = Target
        fields = ("id", "name", "notes", "country", "completed")

    def update(self, instance, validated_data):
        if instance.completed and validated_data["notes"] != instance.notes:
            raise ValidationError("Cannot update notes of a completed target.")
        return super().update(instance, validated_data)