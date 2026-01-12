from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from missions.models import Mission
from missions.serializers import MissionListCreateSerializer, MissionRetrieveUpdateDestroySerializer
from rest_framework.exceptions import ValidationError


class MissionListCreateView(ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionListCreateSerializer
    name = "Mission list create"


class MissionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionRetrieveUpdateDestroySerializer
    name = "Mission retrieve update destroy"
    lookup_field = "id"

    def perform_destroy(self, instance: Mission) -> None:
        if instance.cat is not None:
            raise ValidationError(
                "Cannot delete a mission assigned to a cat"
            )
        instance.delete()

