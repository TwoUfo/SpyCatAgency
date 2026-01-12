from django.db.models import CharField, DecimalField

from cats.validators import validate_breed
from common.models import UUIDModel
from common.constants import (
    STR_SMALL_MAX_LENGTH,
    MAX_DIGITS,
    DECIMAL_PLACES,
)


class Cat(UUIDModel):
    name = CharField(max_length=STR_SMALL_MAX_LENGTH)
    expirience = DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    salary = DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    breed = CharField(max_length=STR_SMALL_MAX_LENGTH, validators=[validate_breed])
