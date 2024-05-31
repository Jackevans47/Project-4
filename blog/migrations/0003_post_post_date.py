# Generated by Django 4.2.13 on 2024-05-31 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_title_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
