# Generated by Django 4.0.5 on 2022-06-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_todoitem_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]