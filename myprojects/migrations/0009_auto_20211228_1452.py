# Generated by Django 3.2.5 on 2021-12-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likedprojects',
        ),
        migrations.AddField(
            model_name='profile',
            name='likedprojects',
            field=models.ManyToManyField(to='myprojects.myprojects'),
        ),
    ]
