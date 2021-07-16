# Generated by Django 3.2.5 on 2021-07-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('tags', models.CharField(default='', max_length=50)),
                ('handle', models.CharField(default='', max_length=44)),
                ('body', models.CharField(default='', max_length=55)),
            ],
        ),
    ]