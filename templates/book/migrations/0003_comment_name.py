# Generated by Django 3.2.19 on 2023-06-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20230619_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='name', max_length=80),
            preserve_default=False,
        ),
    ]