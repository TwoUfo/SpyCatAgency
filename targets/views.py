from rest_framework.generics import RetrieveUpdateAPIView

from targets.models import Target
from targets.serializers import (
    TargetRetrieveUpdateSerializer,
)


class TargetRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetRetrieveUpdateSerializer
    name = "Target retrieve update"
    lookup_field = "id"
