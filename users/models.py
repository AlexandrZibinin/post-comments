from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="почта")
    username = models.CharField(unique=True, max_length=150, verbose_name="Логин")
    password = models.CharField(max_length=250, verbose_name="Пароль")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="Телефон")
    date_of_birth = models.DateField(verbose_name="Дата рождения", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

