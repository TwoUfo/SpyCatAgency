from django.core.exceptions import ValidationError
from django.db.models import (
    BooleanField,
    OneToOneField,
    CASCADE,
)

from cats.models import Cat
from common.models import UUIDModel


class Mission(UUIDModel):
    completed = BooleanField(default=False)
    cat = OneToOneField(
        Cat,
        on_delete=CASCADE,
        related_name="mission",
        null=True,
        blank=True
    )
