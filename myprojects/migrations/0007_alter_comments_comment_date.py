# Generated by Django 3.2.5 on 2021-12-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0006_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]