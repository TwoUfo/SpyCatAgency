import requests
from django.core.exceptions import ValidationError

def validate_breed(value: str) -> None:
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    response.raise_for_status()

    breeds = {breed["name"] for breed in response.json()}

    if value not in breeds:
        raise ValidationError(f"Breed '{value}' is not supported")
