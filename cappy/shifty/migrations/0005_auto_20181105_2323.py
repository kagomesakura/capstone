# Generated by Django 2.1.2 on 2018-11-05 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifty', '0004_auto_20181105_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayoff',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]