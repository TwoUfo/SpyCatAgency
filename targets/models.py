from django.db.models import CharField, ForeignKey, CASCADE, BooleanField

from common.models import UUIDModel
from common.constants import (
    STR_SMALL_MAX_LENGTH,
)
from missions.models import Mission


class Target(UUIDModel):
    name = CharField(max_length=STR_SMALL_MAX_LENGTH)
    country = CharField(max_length=STR_SMALL_MAX_LENGTH)
    notes = CharField(max_length=STR_SMALL_MAX_LENGTH, null=True, blank=True)
    completed = BooleanField(default=False)
    mission = ForeignKey(
        Mission,
        on_delete=CASCADE,
        related_name="targets",
    )
