# Generated by Django 2.2.3 on 2019-08-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=200)),
                ('temp', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
            ],
        ),
    ]