# Generated by Django 5.1 on 2024-08-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cratefrom', '0002_studentquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquery',
            name='stu_query',
            field=models.TextField(),
        ),
    ]
