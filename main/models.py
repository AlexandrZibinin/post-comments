from django.db import models

from config.settings import NULLABLE, AUTH_USER_MODEL
from users.models import User


class Post(models.Model):
    """модель постов"""

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="main/", verbose_name="Изображение", **NULLABLE)
    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор", related_name="author_post"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования", **NULLABLE
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """модель комментария"""

    post = models.ForeignKey(
        Post, verbose_name="Пост", on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="author_comment",
    )
    text = models.CharField(max_length=250, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования", **NULLABLE
    )

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
