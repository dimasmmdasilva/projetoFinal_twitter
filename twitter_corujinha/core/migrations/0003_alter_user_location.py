# Generated by Django 5.1.1 on 2024-10-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_comment_options_alter_follow_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="location",
            field=models.CharField(
                blank=True,
                default="A definir",
                max_length=100,
                null=True,
                verbose_name="Localização",
            ),
        ),
    ]
