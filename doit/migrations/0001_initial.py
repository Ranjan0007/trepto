# Generated by Django 5.1.4 on 2024-12-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SGXNifty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_trade', models.CharField(max_length=100)),
                ('change', models.CharField(max_length=100)),
                ('change_percent', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
