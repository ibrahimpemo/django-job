# Generated by Django 3.1.1 on 2020-09-24 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='', max_length=50, verbose_name='Job Type'),
            preserve_default=False,
        ),
    ]
