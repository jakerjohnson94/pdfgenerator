# Generated by Django 2.1.7 on 2019-03-25 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdfgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Uploader'),
        ),
    ]
