# Generated by Django 3.2.18 on 2023-02-24 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yannjuApp', '0002_question_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='auth',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
