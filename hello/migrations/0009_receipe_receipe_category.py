# Generated by Django 5.0.6 on 2024-07-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_delete_car_delete_person_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_category',
            field=models.CharField(choices=[('starters', 'Starters'), ('main_course', 'Main Course'), ('desserts', 'Desserts')], default='null', max_length=20),
        ),
    ]
