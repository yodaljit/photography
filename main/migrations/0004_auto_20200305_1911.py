# Generated by Django 3.0.2 on 2020-03-05 13:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200305_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Feautured', 'Featured'), ('People', 'People'), ('Travel', 'Travel'), ('Nature', 'Nature'), ('Animal', 'Animal')], max_length=10),
        ),
    ]
