# Generated by Django 3.2.6 on 2022-09-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='...', max_length=200)),
                ('email', models.CharField(default='...', max_length=200)),
                ('name', models.CharField(default='...', max_length=200)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
