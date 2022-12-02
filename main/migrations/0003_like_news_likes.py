# Generated by Django 4.1.3 on 2022-11-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="Like",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("user", models.CharField(default="anuj04", max_length=50)),
                ("article_id", models.CharField(max_length=300)),
            ],
            options={
                "verbose_name_plural": "Likes",
            },
        ),
        migrations.AddField(
            model_name="news",
            name="likes",
            field=models.BigIntegerField(default=0),
        ),
    ]