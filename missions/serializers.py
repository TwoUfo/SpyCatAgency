from typing import Any, Sequence

from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    PrimaryKeyRelatedField,
    Serializer,
)

from missions.models import Mission
from targets.models import Target
from targets.serializers import TargetListCreateSerializer


class MissionTargetsSerializer(Serializer):
    targets = TargetListCreateSerializer(many=True)

    def validate_targets(self, value: Sequence[dict[str, Any]]) -> Sequence[dict[str, Any]]:
        if not 1 <= len(value) <= 3:
            raise ValidationError("A mission must have between 1 and 3 targets.")
        return value


class MissionListCreateSerializer(ModelSerializer[Mission]):
    targets = MissionTargetsSerializer(write_only=True)
    targets_read = TargetListCreateSerializer(source="targets", many=True, read_only=True)

    class Meta:
        model = Mission
        fields = ("id", "cat", "targets", "targets_read")

    def create(self, validated_data: dict[str, Any]) -> Mission:
        targets_payload = validated_data.pop("targets")["targets"]
        mission = Mission.objects.create(**validated_data)

        Target.objects.bulk_create(
            [Target(mission=mission, **target_data) for target_data in targets_payload]
        )

        return mission


class MissionRetrieveUpdateDestroySerializer(ModelSerializer[Mission]):
    targets = TargetListCreateSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Mission
        fields = ("id", "cat", "completed", "targets")



