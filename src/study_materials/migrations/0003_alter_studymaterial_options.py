# Generated by Django 5.1.7 on 2025-03-19 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_materials', '0002_alter_studymaterial_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studymaterial',
            options={'verbose_name': 'Study Material', 'verbose_name_plural': 'Study Materials'},
        ),
    ]
