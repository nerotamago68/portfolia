# Generated by Django 5.0.6 on 2024-07-05 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Ryan', max_length=100)),
                ('college', models.CharField(default='Marinduque State College', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
