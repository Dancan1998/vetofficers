# Generated by Django 3.1.5 on 2021-01-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20210116_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='VetOfficers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('county', models.CharField(default='', max_length=150)),
                ('published', models.BooleanField(default=False)),
                ('phone_no', models.IntegerField()),
                ('id_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
