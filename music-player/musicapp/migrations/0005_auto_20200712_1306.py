# Generated by Django 3.0.6 on 2020-07-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_recent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AddField(
            model_name='song',
            name='language',
            field=models.CharField(choices=[('Hindi', 'Hindi'), ('English', 'English')], default='Hindi', max_length=20),
        ),
    ]
