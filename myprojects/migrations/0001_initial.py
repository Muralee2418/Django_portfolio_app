# Generated by Django 3.2.5 on 2021-12-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myprojects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('technology', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.FilePathField(path='\\img')),
            ],
        ),
    ]