# Generated by Django 4.2 on 2023-05-03 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emailsapp', '0002_alter_email_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='status',
        ),
        migrations.AddField(
            model_name='email',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
