# Generated by Django 4.1.6 on 2023-02-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_alter_process_assigment_alter_process_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
