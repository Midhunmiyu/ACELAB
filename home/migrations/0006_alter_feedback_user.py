# Generated by Django 4.1.7 on 2023-03-07 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
