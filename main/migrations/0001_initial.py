# Generated by Django 3.0.2 on 2020-03-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('tag', models.CharField(max_length=10)),
                ('author', models.CharField(default='Arthur Rose', max_length=10)),
            ],
        ),
    ]
