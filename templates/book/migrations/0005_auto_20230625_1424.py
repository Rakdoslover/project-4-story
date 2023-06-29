# Generated by Django 3.2.19 on 2023-06-25 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0004_alter_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE,
                related_name='comment_owner', to='auth.user'
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False,
                verbose_name='ID'
            ),
        ),
    ]
