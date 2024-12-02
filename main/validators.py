from rest_framework.exceptions import ValidationError

allowed_resource = ["ерунда", "глупость", "чепуха"]


def validate_title(value):
    value = value.split(" ")
    if value in allowed_resource:
        raise ValidationError("Недопустимый заголовок")
