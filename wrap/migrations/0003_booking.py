# Generated by Django 4.0.4 on 2023-03-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
