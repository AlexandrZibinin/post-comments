# Generated by Django 5.1.3 on 2024-12-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=250, verbose_name="Пароль"),
        ),
    ]
