# Generated by Django 2.0 on 2018-01-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_big', models.CharField(max_length=50)),
                ('title_after_big', models.CharField(default='', max_length=50)),
                ('title_small', models.CharField(default='', max_length=50)),
                ('img_bg', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('ordering', models.IntegerField(default=1)),
            ],
        ),
    ]
