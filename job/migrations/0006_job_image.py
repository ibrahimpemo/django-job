# Generated by Django 3.1.1 on 2020-09-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
