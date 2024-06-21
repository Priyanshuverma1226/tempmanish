# Generated by Django 4.1.13 on 2024-06-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('region', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('loc', models.CharField(max_length=50, null=True)),
                ('org', models.CharField(max_length=50, null=True)),
                ('postal', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
