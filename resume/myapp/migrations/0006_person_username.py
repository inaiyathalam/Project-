# Generated by Django 4.1.4 on 2023-01-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_person_selfdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
