# Generated by Django 5.0.2 on 2024-03-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ip',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
