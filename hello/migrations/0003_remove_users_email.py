# Generated by Django 5.0.6 on 2024-05-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_users_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
    ]
