# Generated by Django 3.1.5 on 2021-02-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_aboutdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]
