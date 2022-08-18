# Generated by Django 4.1 on 2022-08-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, default='', max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('zip', models.IntegerField(max_length=50)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
    ]
