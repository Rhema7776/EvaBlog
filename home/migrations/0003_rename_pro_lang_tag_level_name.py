# Generated by Django 3.2.7 on 2021-09-20 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_dev_tag_level_tagjob_taglag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag_level',
            old_name='pro_lang',
            new_name='name',
        ),
    ]
