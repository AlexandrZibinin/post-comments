from datetime import date

from rest_framework.exceptions import ValidationError

allowed_resource = ["mail.ru", "yandex.ru"]


def validate_mail(value):
    val_domain = value.split("@")[-1]
    if val_domain not in allowed_resource:
        raise ValidationError("Недопустимая почта")


def validate_pass(value):
    val_pass = value
    if len(val_pass) < 8:
        raise ValidationError("Пароль короткий")


def validate_age(value):
    today = date.today()
    age = (
        today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    )

    if age < 18:
        raise ValidationError({"age": "Пользователь должен быть старше 18 лет."})

    return value
