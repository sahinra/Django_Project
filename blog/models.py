from django.db import models
from django.core.exceptions import ValidationError


def validate_first_letter(name):
    if name.islower():
        raise ValidationError("First letter should be uppercase!")
    return name


class Participants(models.Model):
    firstName = models.CharField(max_length=20, validators=[validate_first_letter])
    lastName = models.CharField(max_length=20, validators=[validate_first_letter])
    title = models.CharField(max_length=120)
