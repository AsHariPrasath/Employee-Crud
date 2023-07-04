# Generated by Django 4.2.2 on 2023-06-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('contactno', models.IntegerField()),
                ('emailid', models.CharField(max_length=25)),
                ('dateofbirth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('jobrole', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
